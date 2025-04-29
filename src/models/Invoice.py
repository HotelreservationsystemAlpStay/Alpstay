from datetime import date

class Invoice:
    def __init__(self, invoice_id: int, booking_id: int, issue_date: date = date.today(), total_amount: float = 0.0):
        self._validate_invoice_id(invoice_id)
        self._validate_booking_id(booking_id)
        self._validate_issue_date(issue_date)
        self._validate_total_amount(total_amount)

        self._invoice_id = invoice_id
        self._booking_id = booking_id
        self._issue_date = issue_date
        self._total_amount = total_amount
        self._paid = False  # additional state

    def _validate_invoice_id(self, invoice_id):
        if not isinstance(invoice_id, int):
            raise ValueError("Invoice ID must be an integer")
        if invoice_id < 1:
            raise ValueError("Invoice ID cannot be negative")

    def _validate_booking_id(self, booking_id):
        if not isinstance(booking_id, int):
            raise ValueError("Booking ID must be an integer")
        if booking_id < 1:
            raise ValueError("Booking ID cannot be negative")

    def _validate_issue_date(self, issue_date):
        if not isinstance(issue_date, date):
            raise ValueError("Issue date must be a date object")
        if issue_date > date.today():
            raise ValueError("Issue date cannot be in the future")

    def _validate_total_amount(self, total_amount):
        if not isinstance(total_amount, (float, int)):
            raise ValueError("Total amount must be a number")
        if total_amount < 0:
            raise ValueError("Total amount cannot be negative")

    # Properties
    @property
    def invoice_id(self):
        return self._invoice_id

    @invoice_id.setter
    def invoice_id(self, new_invoice_id: int):
        self._validate_invoice_id(new_invoice_id)
        self._invoice_id = new_invoice_id

    @property
    def booking_id(self):
        return self._booking_id

    @booking_id.setter
    def booking_id(self, new_booking_id: int):
        self._validate_booking_id(new_booking_id)
        self._booking_id = new_booking_id

    @property
    def issue_date(self):
        return self._issue_date

    @issue_date.setter
    def issue_date(self, new_issue_date: date):
        self._validate_issue_date(new_issue_date)
        self._issue_date = new_issue_date

    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, new_total_amount: float):
        self._validate_total_amount(new_total_amount)
        self._total_amount = new_total_amount

    @property
    def paid(self):
        return self._paid

    # Methods
    def mark_as_paid(self):
        """Markiert die Rechnung als bezahlt."""
        self._paid = True

    def generate_pdf(self):
        """Simuliert die PDF-Generierung."""
        return f"Invoice_{self._invoice_id}.pdf"

    def __str__(self):
        return (f"Invoice(ID={self._invoice_id}, Booking={self._booking_id}, "
                f"Date={self._issue_date}, Amount={self._total_amount}, "
                f"Paid={self._paid})")