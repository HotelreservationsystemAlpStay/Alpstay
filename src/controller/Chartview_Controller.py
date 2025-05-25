from data_Access.Chartview_Access import Chartview_Access

class Chartview_Controller:
    def __init__(self):
        self.Chartview_Access = Chartview_Access()
    
    def get_amount_per_hotel(self):
        result = self.Chartview_Access.amount_per_hotel()
        hotels = []
        for row in result:
            hotel_name = row["name"]
            amount = row["SUM(total_amount)"]
            hotels.append((hotel_name, amount))
        return hotels
