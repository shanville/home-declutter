import csv
import json
from pathlib import Path
from typing import List, Dict


def convert_csv_to_json(csv_path: Path, json_path: Path) -> List[Dict[str, str]]:
    """Convert a CSV file to JSON.

    Parameters
    ----------
    csv_path : Path
        Path to the input CSV file.
    json_path : Path
        Path where the output JSON will be written.

    Returns
    -------
    List[Dict[str, str]]
        Parsed data from the CSV file.
    """
    with csv_path.open(newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        data = list(reader)

    with json_path.open('w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    return data


def main(args=None):
    import argparse

    parser = argparse.ArgumentParser(description="CSV to JSON converter")
    parser.add_argument("csv_file", type=Path, help="Path to the input CSV file")
    parser.add_argument("json_file", type=Path, help="Path to the output JSON file")
    parsed = parser.parse_args(args)

    convert_csv_to_json(parsed.csv_file, parsed.json_file)


if __name__ == "__main__":
    main()
