class Invoice:
    def __init__(self, invoice_id: int, booking_id: int, issue_date: str, total_amount: float):
        self._invoice_id = invoice_id
        self._booking_id = booking_id
        self._issue_date = issue_date
        self._total_amount = total_amount

    @property
    def invoice_id(self):
        return self._invoice_id

    @invoice_id.setter
    def invoice_id(self, new_invoice_id: int):
        self._invoice_id = new_invoice_id

    @property
    def booking_id(self):
        return self._booking_id

    @booking_id.setter
    def booking_id(self, new_booking_id: int):
        self._booking_id = new_booking_id

    @property
    def issue_date(self):
        return self._issue_date

    @issue_date.setter
    def issue_date(self, new_issue_date: str):
        self._issue_date = new_issue_date

    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, new_total_amount: float):
        self._total_amount = new_total_amount

    def __str__(self):
        return f"Invoice {self._invoice_id} for booking {self._booking_id} issued on {self._issue_date} with amount {self._total_amount}"
