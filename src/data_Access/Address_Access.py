import sqlite3
from models.Address import Address

class Address_Access:
    """Class to access and manage address data in the database."""

    def __init__(self):
        """Initialize Address Access."""
        pass

    @staticmethod
    def sqlite3row_to_address(row):
        """Convert SQLite row to Address object."""
        return Address(
            id=int(row['address_id']),
            street=row['street'],
            city=row['city'],
            zip=row['zip_code']
            )