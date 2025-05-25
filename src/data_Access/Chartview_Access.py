from data_Access.Base_Access_Controller import Base_Access_Controller
class Chartview_Access():
    def __init__(self):
        self.db = Base_Access_Controller()
    
    def amount_per_hotel(self):
        query = """
        SELECT name, SUM(total_amount) 
        FROM booking_view 
        GROUP BY name
        HAVING SUM(total_amount) > 0
        """
        return self.db.fetchall(query)

