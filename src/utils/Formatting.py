from datetime import datetime
class Format:
    @staticmethod
    def parse(date):
        """Parse date string in various formats to date object.
        
        Args:
            date (str): Date string in format DD.MM.YYYY, YYYY-MM-DD, or DD/MM/YYYY
            
        Returns:
            date: Parsed date object
            
        Raises:
            ValueError: If date format is not supported
        """
        formats = ["%d.%m.%Y", "%Y-%m-%d", "%d/%m/%Y"]
        for fmt in formats:
            try:
                return datetime.strptime(date, fmt).date()
            except ValueError:
                continue
        raise ValueError("Unsupported date format.")
    @staticmethod
    def date_to_string(date):
        """Convert date object to ISO format string.
        
        Args:
            date: Date object to convert
            
        Returns:
            str: Date in ISO format (YYYY-MM-DD)
        """
        return date.isoformat()