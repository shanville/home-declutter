import csv
import json
from pathlib import Path


def convert_csv_to_json(csv_path: str | Path, json_path: str | Path) -> None:
    """Convert CSV file to JSON list of objects."""
    csv_path = Path(csv_path)
    json_path = Path(json_path)
    with csv_path.open(newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    with json_path.open('w', encoding='utf-8') as f:
        json.dump(rows, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="CSV to JSON converter")
    parser.add_argument("csv_path", help="input CSV file")
    parser.add_argument("json_path", help="output JSON file")
    args = parser.parse_args()
    convert_csv_to_json(args.csv_path, args.json_path)
