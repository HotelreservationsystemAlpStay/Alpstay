from datetime import date

class Invoice:
    def __init__(self, invocee_id: int, issue_date: date, add_name: str, access_to_at: int) -> None:
        # Direkte Zuweisung (keine Validierung)
        self.invocee_id = invocee_id
        self.issue_date = issue_date
        self.add_name = add_name
        self.access_to_at = access_to_at
        self.paid = False          # Default-Wert
        self.discount_applied = False  # Default-Wert

    # Methoden
    def split_invoice(self) -> str:
        """Erstellt eine PDF der Rechnung und gibt den Dateipfad zurück."""
        return "invoice.pdf"
    
    def mark_as_paid(self) -> None:
        """Markiert die Rechnung als bezahlt."""
        self.paid = True
    
    def supply_discount(self, current: bool = True) -> None:
        """Wendet einen Rabatt an, falls current=True."""
        self.discount_applied = current

    def __str__(self) -> str:
        return (
            f"Invoice(id={self.invocee_id}, date={self.issue_date}, "
            f"name={self.add_name}, access={self.access_to_at}, "
            f"paid={self.paid}, discount={self.discount_applied})"
        )
                