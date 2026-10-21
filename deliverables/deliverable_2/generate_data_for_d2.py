"""
Dataset Generator for Campus Coffee Shop Assignment.
Creates nested folders, mixed encoding logs, and nested config JSON.
"""

import json
import random
from datetime import datetime, timedelta
from pathlib import Path

BASE_DIR = Path("C:\\", "Users", "tutor5923", "Documents", "folder_for_saving", "d2_data")  # Path("data")
STORES = ["library_cafe", "science_building", "student_union"]
REGISTERS = ["POS_01", "POS_02", "POS_03"]
CURRENCIES = ["EUR", "NOK", "USD"]
ITEMS = [
    ("Espresso", 3.00),
    ("Latte", 4.50),
    ("Cappuccino", 4.20),
    ("Muffin", 3.50),
    ("Croissant", 3.80),
    ("Sandwich", 7.50),
]
STATUSES = ["SUCCESS", "SUCCESS", "SUCCESS", "SUCCESS", "REFUND", "CANCELLED"]

NOISE_LINES = [
    "--- PRINTER PAPER LOW ---",
    "[DEBUG] BARCODE SCANNER REBOOTED",
    "=== NETWORK SYNC OK ===",
]


def generate_log_line(ts: datetime, reg_id: str) -> str:
    item_name, base_price = random.choice(ITEMS)
    currency = random.choice(CURRENCIES)

    price = 999.00 if random.random() < 0.03 else round(base_price + random.uniform(-0.5, 0.5), 2)
    status = random.choice(STATUSES)
    ts_str = ts.strftime("%Y-%m-%d %H:%M:%S")

    return f"[{ts_str}] [{reg_id}] item={item_name} price={price:.2f} {currency} ({status})\n"


def create_dataset():
    start_time = datetime(2026, 10, 15, 7, 0, 0)
    file_idx = 0

    for store in STORES:
        for reg in REGISTERS:
            folder = BASE_DIR / "2026" / store / reg
            folder.mkdir(parents=True, exist_ok=True)

            log_file = folder / "register_sales.log"
            encoding = "utf-8" if file_idx % 2 == 0 else "iso-8859-1"
            
            lines = []
            current_time = start_time

            for _ in range(80):
                current_time += timedelta(seconds=random.randint(10, 180))
                if random.random() < 0.15:
                    lines.append(random.choice(NOISE_LINES) + "\n")
                lines.append(generate_log_line(current_time, reg))

            with open(log_file, "w", encoding=encoding) as f:
                f.writelines(lines)

            file_idx += 1
            print(f"Generated: {log_file} [{encoding.upper()}]")

    # Generate nested JSON config
    config = {
        "company": "Campus Coffee",
        "regions": [
            {
                "region_name": "Main Campus",
                "stores": [
                    {
                        "name": "Library Cafe",
                        "registers": [
                            {"id": "POS_01", "active": True},
                            {"id": "POS_02", "active": True},
                        ],
                    },
                    {
                        "name": "Science Building",
                        "registers": [
                            {"id": "POS_03", "active": True},
                            {"id": "POS_04", "active": False},
                        ],
                    },
                ],
            }
        ],
    }

    with open(BASE_DIR / "store_config.json", "w", encoding="utf-8") as f:
        json.dump(config, f, indent=2)

    print("\nDataset generation complete!")


if __name__ == "__main__":
    create_dataset()
