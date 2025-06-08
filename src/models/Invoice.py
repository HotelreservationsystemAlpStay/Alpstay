from datetime import date

class Invoice:
    def __init__(self, invoice_id: int, booking_id: int, issue_date: date = None, total_amount: float = 0.0):
        self._invoice_id = invoice_id
        self._booking_id = booking_id
        self._issue_date = issue_date if issue_date is not None else date.today()
        self._total_amount = total_amount

    @property
    def invoice_id(self) -> int:
        return self._invoice_id

    @invoice_id.setter
    def invoice_id(self, new_invoice_id: int) -> None:
        self._invoice_id = new_invoice_id

    @property
    def booking_id(self) -> int:
        return self._booking_id

    @booking_id.setter
    def booking_id(self, new_booking_id: int) -> None:
        self._booking_id = new_booking_id

    @property
    def issue_date(self) -> date:
        return self._issue_date

    @issue_date.setter
    def issue_date(self, new_issue_date: date) -> None:
        self._issue_date = new_issue_date

    @property
    def total_amount(self) -> float:
        return self._total_amount

    @total_amount.setter
    def total_amount(self, new_total_amount: float) -> None:
        self._total_amount = new_total_amount

    def __str__(self):
        return (f"Invoice(ID={self._invoice_id}, Booking={self._booking_id}, "
                f"Date={self._issue_date}, Amount={self._total_amount}, "
                f"Paid={self._paid})")

    def to_dict(self) -> dict:  # Added to_dict for consistency
        return {
            'invoice_id': self._invoice_id,
            'booking_id': self._booking_id,
            'issue_date': self._issue_date.isoformat() if self._issue_date else None,
            'total_amount': self._total_amount,
            'paid': self._paid
        }