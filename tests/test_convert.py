from pathlib import Path
import json

from src.convert import convert_csv_to_json


def test_convert_csv_to_json(tmp_path: Path) -> None:
    csv_file = tmp_path / "input.csv"
    json_file = tmp_path / "output.json"
    csv_file.write_text(
        "category,item,action,notes\n"
        "家具,ベッド,処分,\n"
        "衣類,シャツ,保管,お気に入り\n",
        encoding="utf-8",
    )
    convert_csv_to_json(csv_file, json_file)
    data = json.loads(json_file.read_text(encoding="utf-8"))
    assert data == [
        {"category": "家具", "item": "ベッド", "action": "処分", "notes": ""},
        {"category": "衣類", "item": "シャツ", "action": "保管", "notes": "お気に入り"},
    ]
