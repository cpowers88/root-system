#!/usr/bin/env python3
"""On-demand guard against stale Git worktree overwrites.

Exit 0 means no high-confidence stale-overwrite signal was found. Exit 1 means
one or more files exactly match an older committed version or have materially
shrunk. Exit 2 means the check itself could not run reliably.
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Finding:
    path: str
    kind: str
    detail: str


def git(root: Path, *args: str, check: bool = True) -> bytes:
    result = subprocess.run(
        ["git", "-C", str(root), *args],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if check and result.returncode:
        raise RuntimeError(result.stderr.decode("utf-8", "replace").strip())
    return result.stdout


def changed_paths(root: Path) -> list[str]:
    raw = git(root, "status", "--porcelain=v1", "-z", "--untracked-files=no")
    paths: list[str] = []
    fields = raw.split(b"\0")
    index = 0
    while index < len(fields) and fields[index]:
        record = fields[index]
        status = record[:2]
        path = record[3:].decode("utf-8", "surrogateescape")
        if status[0:1] in {b"R", b"C"}:
            index += 1
            if index < len(fields):
                path = fields[index].decode("utf-8", "surrogateescape")
        if b"D" not in status and path not in paths:
            paths.append(path)
        index += 1
    return paths


def blob(root: Path, revision: str, path: str) -> bytes | None:
    result = subprocess.run(
        ["git", "-C", str(root), "show", f"{revision}:{path}"],
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
        check=False,
    )
    return result.stdout if result.returncode == 0 else None


def same_content(left: bytes, right: bytes) -> bool:
    """Compare text across Git's CRLF checkout normalization; keep binary exact."""
    if b"\0" in left or b"\0" in right:
        return left == right
    return left.replace(b"\r\n", b"\n") == right.replace(b"\r\n", b"\n")


def historical_reversion(root: Path, path: str, current: bytes, limit: int) -> str | None:
    revisions = git(root, "rev-list", f"--max-count={limit}", "HEAD", "--", path)
    commits = revisions.decode("ascii", "replace").splitlines()
    for commit in commits[1:]:  # HEAD/current baseline cannot be a stale reversion.
        prior = blob(root, commit, path)
        if prior is not None and same_content(prior, current):
            return commit[:12]
    return None


def inspect(
    root: Path,
    paths: list[str],
    shrink_percent: int = 35,
    min_removed_lines: int = 20,
    history_limit: int = 50,
) -> list[Finding]:
    findings: list[Finding] = []
    for path in paths:
        disk_path = root / path
        if not disk_path.is_file():
            continue
        current = disk_path.read_bytes()
        head = blob(root, "HEAD", path)
        if head is None or same_content(current, head):
            continue

        old_commit = historical_reversion(root, path, current, history_limit)
        if old_commit:
            findings.append(
                Finding(path, "historical-reversion", f"matches older commit {old_commit}")
            )

        head_lines = len(head.splitlines())
        current_lines = len(current.splitlines())
        removed = head_lines - current_lines
        if head_lines and removed >= min_removed_lines:
            percent = round(removed * 100 / head_lines)
            if percent >= shrink_percent:
                findings.append(
                    Finding(
                        path,
                        "material-shrink",
                        f"{head_lines} -> {current_lines} lines ({percent}% removed)",
                    )
                )
    return findings


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="*", help="Repo-relative tracked files; defaults to current tracked changes")
    parser.add_argument("--root", type=Path, default=Path.cwd(), help="Git working-tree root")
    parser.add_argument("--shrink-percent", type=int, default=35)
    parser.add_argument("--min-removed-lines", type=int, default=20)
    parser.add_argument("--history-limit", type=int, default=50)
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    root = args.root.resolve()
    try:
        repo_root = Path(git(root, "rev-parse", "--show-toplevel").decode().strip()).resolve()
        paths = args.paths or changed_paths(repo_root)
        findings = inspect(
            repo_root,
            paths,
            args.shrink_percent,
            args.min_removed_lines,
            args.history_limit,
        )
    except (OSError, RuntimeError) as exc:
        print(f"STALE OVERWRITE GUARD ERROR: {exc}", file=sys.stderr)
        return 2

    if findings:
        print("STALE OVERWRITE GUARD: BLOCK")
        for finding in findings:
            print(f"  {finding.path}: {finding.kind} — {finding.detail}")
        print("Inspect the diff and recover intentionally before committing.")
        return 1

    print(f"STALE OVERWRITE GUARD: PASS ({len(paths)} tracked changed file(s) checked)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
