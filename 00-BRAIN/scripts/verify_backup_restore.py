#!/usr/bin/env python3
"""Restore a .ROOT backup into an empty test target and verify it.

This is deliberately on-demand. It uses quiet robocopy summaries so the source
and restored 88-JOURNAL trees are copied and counted without listing filenames
or reading file contents. It never deletes the restore target.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path


COMPLETE_MARKER = ".snapshot_complete"
BACKUP_SENTINEL = ".ROOT_BACKUP_ROOT"


def completed_snapshots(root: Path) -> list[Path]:
    if not root.is_dir():
        return []
    return sorted(
        (item for item in root.iterdir() if item.is_dir() and (item / COMPLETE_MARKER).is_file()),
        key=lambda item: item.name,
        reverse=True,
    )


def choose_source(mirror: Path, snapshot_root: Path | None, use_latest_snapshot: bool) -> Path:
    if use_latest_snapshot:
        if snapshot_root is None:
            raise ValueError("--snapshot-root is required with --latest-snapshot")
        snapshots = completed_snapshots(snapshot_root)
        if not snapshots:
            raise ValueError("no completed snapshot is available")
        return snapshots[0]
    if not mirror.is_dir() or not (mirror / BACKUP_SENTINEL).is_file():
        raise ValueError(f"mirror is missing its {BACKUP_SENTINEL} sentinel: {mirror}")
    return mirror


def ensure_empty_target(target: Path) -> None:
    if target.exists() and any(target.iterdir()):
        raise ValueError(f"restore target must be empty: {target}")
    target.mkdir(parents=True, exist_ok=True)


def robocopy(source: Path, target: Path) -> str:
    result = subprocess.run(
        [
            "robocopy", str(source), str(target), "/E", "/COPY:DAT", "/DCOPY:DAT",
            "/R:1", "/W:1", "/XJ", "/NJH", "/NFL", "/NDL", "/BYTES",
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=False,
    )
    if result.returncode >= 8:
        raise RuntimeError(f"robocopy failed with exit {result.returncode}")
    return result.stdout


def summary(output: str) -> tuple[int, int]:
    files = re.search(r"^\s*Files\s*:\s*(\d+)", output, re.MULTILINE)
    size = re.search(r"^\s*Bytes\s*:\s*(\d+)", output, re.MULTILINE)
    if not files or not size:
        raise RuntimeError("robocopy did not return parseable file and byte totals")
    return int(files.group(1)), int(size.group(1))


def verify_git(restore: Path, git_backup: Path | None) -> None:
    pointer = restore / ".git"
    if git_backup:
        if not git_backup.is_dir() or not (git_backup / BACKUP_SENTINEL).is_file():
            raise ValueError(f"gitdir backup is missing its {BACKUP_SENTINEL} sentinel")
        restored_git = restore.parent / f"{restore.name}-git"
        ensure_empty_target(restored_git)
        robocopy(git_backup, restored_git)
        pointer.write_text(f"gitdir: {restored_git}\n", encoding="utf-8")
    if not pointer.exists():
        raise RuntimeError("restored vault has no .git directory or pointer")
    result = subprocess.run(
        ["git", "-C", str(restore), "fsck", "--no-dangling"],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        check=False,
    )
    if result.returncode:
        raise RuntimeError(f"git fsck failed: {result.stdout.strip()}")


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mirror", required=True, type=Path)
    parser.add_argument("--restore-target", required=True, type=Path)
    parser.add_argument("--snapshot-root", type=Path)
    parser.add_argument("--latest-snapshot", action="store_true")
    parser.add_argument("--git-backup", type=Path)
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    try:
        source = choose_source(args.mirror.resolve(), args.snapshot_root, args.latest_snapshot)
        target = args.restore_target.resolve()
        ensure_empty_target(target)
        copied = summary(robocopy(source, target))
        if not (target / "00-BRAIN" / "AGENT.md").is_file():
            raise RuntimeError("restore is missing 00-BRAIN\\AGENT.md")
        verify_git(target, args.git_backup.resolve() if args.git_backup else None)
    except (OSError, RuntimeError, ValueError) as exc:
        print(f"RESTORE VERIFICATION: FAIL — {exc}", file=sys.stderr)
        return 1
    print(f"RESTORE VERIFICATION: PASS — {copied[0]} files, {copied[1]} bytes; git fsck clean")
    print(f"Restored test tree retained at: {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
