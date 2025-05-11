class RoomAccess():



    #Idee:
    @staticmethod
    def _get_season(date_obj:date):
    
        date_str = date_obj.strftime("%m-%d")
        summer_start = "04-01"
        summer_end = "09-30"
        winter_start = "10-01"
        winter_end = "03-31"

        if summer_start <= date_str <= summer_end:
            return "Summer"
        elif winter_start <= date_str or date_str <= winter_end:
            return "Winter"

    def calculate_days(start_date, end_date):
       
        days = end_date - start_date
        



    

    def __init__(self, summer:float, winter:float):
        self._summer = summer
        self._winter = winter

    def set_price(self,price:float, season:str):
        if season == "summer":
            return price*self._summer
        else: 
            return price*self._winter
        
roomAccess = RoomAccess(1.9, 1.0)
print(roomAccess.set_price(150, "summer"))