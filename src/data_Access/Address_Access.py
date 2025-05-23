import sqlite3
from models.Address import Address

class Address_access:
    def __init__(self):
        pass

    @staticmethod
    def sqlite3row_to_address(row):
        return Address(
            id=row['address_id'],
            street=row['street'],
            city=row['city'],
            zip=row['zip_code']
            )