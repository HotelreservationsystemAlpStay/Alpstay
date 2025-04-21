from datetime import date

class Invoice:
    def __init__(self, invoice_id: int, issue_date: date, client_name: str, access_code: int):
        self._validate_invoice_id(invoice_id)
        self._validate_issue_date(issue_date)
        self._validate_client_name(client_name)
        self._validate_access_code(access_code)

        self._invoice_id = invoice_id
        self._issue_date = issue_date
        self._client_name = client_name
        self._access_code = access_code
        self._paid = False
        self._discount_applied = False

    # --- Validierungsmethoden ---
    def _validate_invoice_id(self, invoice_id: int) -> None:
        if not isinstance(invoice_id, int):
            raise ValueError("Invoice ID must be an integer")
        if invoice_id < 1:
            raise ValueError("Invoice ID cannot be negative")

    def _validate_issue_date(self, issue_date: date) -> None:
        if not isinstance(issue_date, date):
            raise ValueError("Issue date must be a date object")
        if issue_date > date.today():
            raise ValueError("Issue date cannot be in the future")

    def _validate_client_name(self, client_name: str) -> None:
        if not isinstance(client_name, str):
            raise ValueError("Client name must be a string")
        if client_name.strip() == "":
            raise ValueError("Please enter a client name")

    def _validate_access_code(self, access_code: int) -> None:
        if not isinstance(access_code, int):
            raise ValueError("Access code must be an integer")
        if access_code < 0:
            raise ValueError("Access code cannot be negative")

    # --- Properties ---
    @property
    def invoice_id(self) -> int:
        return self._invoice_id

    @invoice_id.setter
    def invoice_id(self, new_id: int) -> None:
        self._validate_invoice_id(new_id)
        self._invoice_id = new_id

    @property
    def issue_date(self) -> date:
        return self._issue_date

    @issue_date.setter
    def issue_date(self, new_date: date) -> None:
        self._validate_issue_date(new_date)
        self._issue_date = new_date

    @property
    def client_name(self) -> str:
        return self._client_name

    @client_name.setter
    def client_name(self, new_name: str) -> None:
        self._validate_client_name(new_name)
        self._client_name = new_name

    @property
    def access_code(self) -> int:
        return self._access_code

    @access_code.setter
    def access_code(self, new_code: int) -> None:
        self._validate_access_code(new_code)
        self._access_code = new_code

    @property
    def paid(self) -> bool:
        return self._paid

    @property
    def discount_applied(self) -> bool:
        return self._discount_applied

    # --- Methoden ---
    def mark_as_paid(self) -> None:
        """Markiert die Rechnung als bezahlt."""
        self._paid = True

    def apply_discount(self, discount: bool = True) -> None:
        """Wendet einen Rabatt an oder entfernt ihn."""
        self._discount_applied = discount

    def generate_pdf(self) -> str:
        """Simuliert die PDF-Erstellung und gibt einen Dateipfad zurück."""
        return f"invoice_{self._invoice_id}.pdf"

    def __str__(self) -> str:
        return (f"Invoice ID: {self._invoice_id}, "
                f"Client: {self._client_name}, "
                f"Issue Date: {self._issue_date}, "
                f"Status: {'Paid' if self._paid else 'Unpaid'}, "
                f"Discount: {'Applied' if self._discount_applied else 'None'}")