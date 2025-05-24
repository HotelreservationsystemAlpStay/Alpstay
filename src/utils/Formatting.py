from datetime import datetime
class Format:
    @staticmethod
    def parse(date):
        formats = ["%d.%m.%Y", "%Y-%m-%d", "%d/%m/%Y"]
        for fmt in formats:
            try:
                return datetime.strptime(date, fmt).date()
            except ValueError:
                continue
        raise ValueError("Unsupported date format.")
    @staticmethod
    def date_to_string(date):
        return date.isoformat()