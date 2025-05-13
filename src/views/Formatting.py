class Format:
    @staticmethod
    def parse(input_str):
        formats = ["%d.%m.%Y", "%Y-%m-%d", "%d/%m/%Y"]
        for fmt in formats:
            try:
                return datetime.strptime(input_str, fmt).date()
            except ValueError:
                continue
        raise ValueError("Unsupported date format.")