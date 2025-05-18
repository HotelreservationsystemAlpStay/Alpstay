class Hotel_Controller:
    def __init__(self):
        self.query = """
        SELECT DISTINCT hotel_id, name, stars, city, street
        FROM extended_hotel_room_booking
        WHERE 1=1
        """
        self.WHERE_CITY = "WHERE city = ?"
    def get_information(self):
        return "Hello"
    def get_hotels(self, city=None, stars=None):
        is_inloop = False
        param = []
        if city:
            if is_inloop:
                self.query += f" AND {self.WHERE_CITY}"
            else:
                self.query += f" {self.WHERE_CITY}"
            param.append(city)
        if stars:
            pass
        return
            