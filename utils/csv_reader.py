import csv
from pathlib import Path


def read_csv(file_path):
    path = Path(file_path)
    if not path.is_absolute():
        path = Path(__file__).resolve().parent.parent / path

    rows = []
    with path.open(newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            rows.append(
                {
                    "username": row["username"].strip(),
                    "password": row["password"].strip(),
                    "expected": row["expected"].strip(),
                }
            )
    return rows
