from data_Access.Base_Access_Controller import Base_Access_Controller

class Guest_Access:
    def __init__(self):
        self.db = Base_Access_Controller()

    def access_guest_ages(self):
        """
        Fetches the ages of all guests.
        Assumes a 'Guest' table with an 'age' column.
        """
        query = "SELECT age FROM Guest WHERE age IS NOT NULL;"
        return self.db.fetchall(query)

    def access_guest_countries(self):
        """
        Fetches the distribution of guests by country.
        Assumes a 'Guest' table with a 'country' column.
        """
        query = """
            SELECT country, COUNT(*) AS guest_count
            FROM Guest
            WHERE country IS NOT NULL AND country != ''
            GROUP BY country
            ORDER BY guest_count DESC;
        """
        return self.db.fetchall(query)

    def access_guest_booking_frequency(self):
        """
        Fetches counts of new and returning guests.
        A guest is returning if they have more than one booking.
        Assumes a 'Booking' table with a 'guest_id' column.
        """
        query_new_guests = """
            SELECT COUNT(*) as count
            FROM (
                SELECT guest_id
                FROM Booking
                GROUP BY guest_id
                HAVING COUNT(booking_id) = 1
            );
        """
        new_guests_row = self.db.fetchone(query_new_guests)
        new_guests_count = new_guests_row['count'] if new_guests_row else 0

        query_returning_guests = """
            SELECT COUNT(*) as count
            FROM (
                SELECT guest_id
                FROM Booking
                GROUP BY guest_id
                HAVING COUNT(booking_id) > 1
            );
        """
        returning_guests_row = self.db.fetchone(query_returning_guests)
        returning_guests_count = returning_guests_row['count'] if returning_guests_row else 0
        
        return {'new_guests': new_guests_count, 'returning_guests': returning_guests_count}