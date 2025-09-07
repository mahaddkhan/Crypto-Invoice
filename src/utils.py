import os
from datetime import datetime

COUNTER_FILE = "invoice_counter.txt"

def generate_invoice_number():
    if not os.path.exists(COUNTER_FILE):
        last_number = 0
    else:
        with open(COUNTER_FILE, "r") as f:
            last_number = int(f.read().strip())

    new_number = last_number + 1

    with open(COUNTER_FILE, "w") as f:
        f.write(str(new_number))

    return f"INV{new_number:07d}"

def get_invoice_date():
    date_input = input("Enter invoice date (YYYY-MM-DD) [Leave empty for today]: ").strip()
    if not date_input:
        return datetime.now().strftime('%Y-%m-%d')
    return date_input
