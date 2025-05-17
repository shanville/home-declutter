from pathlib import Path
import json
import tempfile
from src.convert import convert_csv_to_json


SAMPLE_CSV = Path(__file__).parents[1] / 'data' / 'checklist.csv'


def test_convert_csv_to_json(tmp_path: Path):
    output_json = tmp_path / 'out.json'
    data = convert_csv_to_json(SAMPLE_CSV, output_json)

    assert output_json.exists()
    with output_json.open(encoding='utf-8') as f:
        loaded = json.load(f)

    assert data == loaded
    assert len(loaded) == 3
    assert loaded[0]['category'] == '家具'
