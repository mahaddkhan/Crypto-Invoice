from price_fetcher import get_price
from pdf_generator import create_invoice
from utils import generate_invoice_number, get_invoice_date

def main():
    print("\n=== Crypto Invoice Generator ===\n")

    client_name = input("Enter client name: ").strip() or "Unknown Client"
    wallet_address = input("Enter crypto wallet address (optional, press Enter to skip): ").strip() or None
    days = input("How many days until the invoice is due? (Leave blank for today): ")

    if days == "":
        due_days = 0
    else:
        try:
            due_days = int(days)
            if due_days < 0:
                print("❌ Number of days cannot be negative. Setting due today.")
                due_days = 0
        except ValueError:
            print("❌ Invalid input. Setting due today.")
            due_days = 0

    invoice_number = generate_invoice_number()
    invoice_date = get_invoice_date()

    invoice_items = []

    print("\nEnter crypto coins and amounts. Type 'done' when finished.")
    while True:
        coin = input("Coin (e.g., bitcoin): ").upper()
        if coin == "DONE":
            break
        if not coin.isalpha():
            print("❌ Coin must contain only letters.")
            continue
        try:
            amount = float(input(f"Amount of {coin}: "))
        except ValueError:
            print("❌ Enter a valid number.")
            continue

        price = get_price(coin)
        total = amount * price
        invoice_items.append({"coin": coin, "amount": amount, "price": price, "total": total})

    fee_percent = None
    fee_input = input("Do you want to add a % fee? (optional, press Enter to skip): ").strip()
    if fee_input:
        try:
            fee_percent = float(fee_input)
        except ValueError:
            fee_percent = None

    create_invoice(invoice_items, client_name, wallet_address, invoice_number, invoice_date, fee_percent, days_due=due_days)

if __name__ == "__main__":
    main()
