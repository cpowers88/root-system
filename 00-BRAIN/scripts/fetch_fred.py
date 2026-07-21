"""Fetch a curated set of FRED series into CSVs. Reads the API key from
C:\\Users\\chris\\.root-secrets\\FRED.env at runtime; never prints the key."""
import csv
import json
import os
import urllib.request
import urllib.error

ENV_PATH = r"C:\Users\chris\.root-secrets\FRED.env"
OUT_DIR = r"C:\Users\chris\.ROOT\02-LIBRARY\00-SCHOOL\04-ECON\datasets"

SERIES = {
    "GDP": "Gross Domestic Product (nominal, quarterly, billions $)",
    "GDPC1": "Real Gross Domestic Product (chained 2017 dollars, quarterly)",
    "CPIAUCSL": "Consumer Price Index for All Urban Consumers (monthly, inflation)",
    "UNRATE": "Unemployment Rate (monthly, percent, seasonally adjusted)",
}


def load_key(path):
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if "=" in line:
                return line.split("=", 1)[1].strip().strip('"').strip("'")
    raise RuntimeError("No key=value line found in env file")


def fetch_series(series_id, api_key):
    url = (
        "https://api.stlouisfed.org/fred/series/observations"
        f"?series_id={series_id}&api_key={api_key}&file_type=json"
    )
    req = urllib.request.Request(url, headers={"User-Agent": "root-vault-fetch/1.0"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        data = json.loads(resp.read().decode("utf-8"))
    return data.get("observations", [])


def main():
    api_key = load_key(ENV_PATH)
    os.makedirs(OUT_DIR, exist_ok=True)
    for series_id, description in SERIES.items():
        try:
            obs = fetch_series(series_id, api_key)
        except urllib.error.HTTPError as e:
            print(f"{series_id}: HTTP error {e.code}")
            continue
        clean = [o for o in obs if o.get("value") not in (".", None)]
        out_path = os.path.join(OUT_DIR, f"{series_id}.csv")
        with open(out_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["date", "value"])
            for o in clean:
                writer.writerow([o["date"], o["value"]])
        first_date = clean[0]["date"] if clean else "n/a"
        last_date = clean[-1]["date"] if clean else "n/a"
        print(f"{series_id}: {len(clean)} observations, {first_date} to {last_date} -> {out_path}")


if __name__ == "__main__":
    main()
