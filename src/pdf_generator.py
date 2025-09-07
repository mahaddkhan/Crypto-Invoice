from fpdf import FPDF
import os
import qrcode
from datetime import datetime, timedelta

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INVOICE_FOLDER = os.path.join(PROJECT_ROOT, "invoices")
os.makedirs(INVOICE_FOLDER, exist_ok=True)

class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 28)
        self.cell(0, 15, "Crypto Invoice", ln=True, align="C")
        self.ln(3)
        self.set_draw_color(180, 180, 180)
        self.set_line_width(0.5)
        self.line(10, 30, 200, 30)
        self.ln(5)

    def footer(self):
        self.set_y(-20)
        self.set_font("Arial", "I", 10)
        self.set_text_color(100, 100, 100)
        self.cell(0, 5, "Thank you for your business!", align="C")

def create_invoice(invoice_items, client_name, wallet_address=None, invoice_number=None, invoice_date=None, fee_percent=None, days_due=0):
    pdf = PDF()
    pdf.add_page()
    pdf.set_font("Arial", "", 12)
    pdf.set_text_color(0, 0, 0)

    if invoice_number is None:
        invoice_number = f"INV{datetime.now().strftime('%Y%m%d%H%M%S')}"
    if invoice_date is None:
        invoice_date = datetime.now().strftime("%Y-%m-%d")

    due_date = (datetime.now() + timedelta(days=days_due)).strftime("%Y-%m-%d")

    # Metadata
    pdf.set_font("Arial", "B", 12)
    pdf.cell(30, 8, "Invoice #: ", ln=0)
    pdf.set_font("Arial", "", 12)
    pdf.cell(0, 8, invoice_number, ln=1)

    pdf.set_font("Arial", "B", 12)
    pdf.cell(30, 8, "Date: ", ln=0)
    pdf.set_font("Arial", "", 12)
    pdf.cell(0, 8, invoice_date, ln=1)

    pdf.set_font("Arial", "B", 12)
    pdf.cell(30, 8, "Due Date: ", ln=0)
    pdf.set_font("Arial", "", 12)
    pdf.cell(0, 8, due_date, ln=1)

    pdf.set_font("Arial", "B", 12)
    pdf.cell(30, 8, "Client Name: ", ln=0)
    pdf.set_font("Arial", "", 12)
    pdf.cell(0, 8, client_name, ln=1)

    pdf.ln(3)
    pdf.set_draw_color(180, 180, 180)
    pdf.set_line_width(0.3)
    pdf.line(10, pdf.get_y(), 200, pdf.get_y())
    pdf.ln(5)

    # Table headings
    pdf.set_font("Arial", "B", 14)
    pdf.cell(50, 8, "Coin", ln=0, align="L")
    pdf.cell(40, 8, "Amount", ln=0, align="L")
    pdf.cell(50, 8, "Price (USD)", ln=0, align="R")
    pdf.cell(50, 8, "Total (USD)", ln=1, align="R")

    # Items
    pdf.set_font("Arial", "", 12)
    total_amount = 0
    for item in invoice_items:
        pdf.cell(50, 8, item["coin"], ln=0, align="L")
        pdf.cell(40, 8, str(item["amount"]), ln=0, align="L")
        pdf.cell(50, 8, f"${item['price']:.2f}", ln=0, align="R")
        pdf.cell(50, 8, f"${item['total']:.2f}", ln=1, align="R")
        total_amount += item['total']

    pdf.ln(5)
    pdf.line(10, pdf.get_y(), 200, pdf.get_y())
    pdf.ln(5)

    # Optional fee
    fee_amount = 0
    if fee_percent is not None:
        fee_amount = total_amount * (fee_percent / 100)

    # Summary (dynamic based on fee)
    grand_total = total_amount + fee_amount
    pdf.set_font("Arial", "B", 12)

    if fee_percent is not None:
        pdf.cell(0, 8, f"Total: ${total_amount:.2f}", ln=1, align="R")
        pdf.cell(0, 8, f"Fee ({fee_percent}%): ${fee_amount:.2f}", ln=1, align="R")

    pdf.cell(0, 8, f"Grand Total: ${grand_total:.2f}", ln=1, align="R")
    pdf.ln(5)

    # Wallet + Functional QR code
    if wallet_address:
        pdf.set_font("Arial", "B", 12)
        pdf.cell(0, 8, "Wallet Address:", ln=1)
        pdf.set_font("Arial", "", 12)
        pdf.multi_cell(0, 6, wallet_address)
        pdf.ln(3)

        qr_data = f"wallet_address".strip()
        qr = qrcode.QRCode(box_size=10, border=2) 
        qr.add_data(qr_data)
        qr.make(fit=True)
        qr_img = qr.make_image(fill_color="black", back_color="white").convert("RGB")

        qr_path = os.path.join(INVOICE_FOLDER, "temp_qr.png")
        qr_img.save(qr_path)

        pdf.image(qr_path, x=pdf.get_x(), y=pdf.get_y(), w=30)
        os.remove(qr_path)
        pdf.ln(35)

    pdf.line(10, pdf.get_y(), 200, pdf.get_y())

    # Save PDF
    pdf_file = os.path.join(INVOICE_FOLDER, f"{invoice_number}.pdf")
    pdf.output(pdf_file)
    print(f"\n✅ Invoice saved as: {os.path.abspath(pdf_file)}\n")