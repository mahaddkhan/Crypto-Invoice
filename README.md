# 🪙 Crypto Invoice Generator

![Python](https://img.shields.io/badge/Python-3.11-blue)

A clean and professional **cryptocurrency invoice generator** built with Python.  
Generate beautifully formatted PDF invoices for crypto transactions with optional fees, wallet addresses, and functional high-resolution QR codes.

---

## 💡 Features

- **Minimalistic, professional PDF layout**  
- Automatically generates **incremental invoice numbers**  
- **Optional percentage-based fee** displayed above Grand Total  
- Supports **multiple cryptocurrencies** in one invoice  
- **Functional QR code** linking directly to the crypto wallet  
- Clean **terminal interaction** for easy invoice creation  
- PDFs saved automatically in an `invoices` folder  
- Configurable **due dates** and **client information**  

---

## 📂 Project Structure

```
crypto_invoice/
│
├── src/
│ ├── main.py # Main script to run the generator
│ ├── pdf_generator.py # Handles PDF creation and QR codes
│ ├── price_fetcher.py # Fetches crypto prices from API
│ ├── utils.py # Helper functions (invoice number, date)
│
├── invoices/ # Generated invoices saved here
├── README.md
└── requirements.txt
```

---

## ⚡ Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/crypto_invoice.git
cd crypto_invoice
```

2. Create a virtual environement (optional but recommended):

```
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

> Dependencies: fpdf, qrcode, requests

---

## 🏃 Usage

Run the main script:

```bash
python src/main.py
```

1. Enter client name
2. Add cryptocurrencies and amounts (e.g., BTC, ETH)
3. Optionally, enter a percentage fee
4. Optionally, provide a wallet address for QR code
5. PDF invoice will be generated in the invoices/ folder

### Example Terminal Flow
```bash
=== Crypto Invoice Generator ===

Enter client name: Alice
Enter crypto coins and amounts. Type 'done' when finished.
Coin (e.g., BTC): BTC
Amount of BTC: 1
Added: BTC - 1 units at $111293.00 each (Total: $111293.00)

Coin (e.g., BTC): ETH
Amount of ETH: 2
Added: ETH - 2 units at $4301.73 each (Total: $8603.46)

Coin (e.g., BTC): done
Do you want to add a percentage fee? (yes/no): yes
Enter fee %: 0.3
Do you want to add a wallet address for QR code? (yes/no): yes
Enter wallet address: bc1qusryd800h9k8yq55z3jgyp583yhm5g6q2406l5

✅ Invoice saved as: /path/to/invoices/INV000010.pdf
```

## 🖼 PDF Layout

- **Header:** "Crypto Invoice" (large, centered)  
- **Invoice metadata:** Invoice #, Date, Due Date, Client Name  
- **Table:** Coin, Amount, Price, Total  
- **Summary:** Total, Fee (optional), Grand Total  
- **Wallet:** Optional wallet address + functional QR code  
- **Footer:** “Thank you for your business!”  

> Minimalistic, professional, and printer-friendly.

---

## 🔧 Customization

- Change **invoice numbering** or reset counter via `invoice_counter.txt`  
- Adjust **PDF colors, fonts, or layout** in `pdf_generator.py`  
- Support additional crypto types by modifying the **QR coin type**

---