from datetime import date

from app.models.invoice import Invoice
from app.service.invoice_check_service import check_invoice


invoice = Invoice(
    invoice_number="RE-1001",
    supplier_name="Muster GmbH",
    amount=15000,
    currency="EUR",
    invoice_date=date(2026, 5, 1),
    due_date=date(2026, 6, 1)
)

result = check_invoice(invoice)

print(result.model_dump())