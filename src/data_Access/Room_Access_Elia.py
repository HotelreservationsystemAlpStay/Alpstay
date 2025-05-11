class RoomAccess():


    @staticmethod
    def _get_seasonal_multiplier(season:str):
        pass
        if season == "Summer":
            return 1.5
        elif season == "Winter":
            return 1.0 

    #Idee:
    @staticmethod
    def _get_season(date:date):
    
        date_now = date.strftime("%m-%d")
        summer_start = "04-01"
        summer_end = "09-30"
        winter_start = "10-01"
        winter_end = "03-31"

        if summer_start <= date_now <= summer_end:
            return "Summer"
        elif winter_start <= date_now or date_now <= winter_end:
            return "Winter"

    @staticmethod
    def _calculate_days(start_date, end_date):
        days = (end_date - start_date).days
        return days
        
    def __init__(self, summer:float, winter:float):
        self._summer = summer
        self._winter = winter

    def set_price(self,price:float, season:str):
        if season == "summer":
            return price*self._summer
        else: 
            return price*self._winter
    
    def price_per_stay():
        # def set_price * days oder so
        
roomAccess = RoomAccess(1.9, 1.0)
print(roomAccess.set_price(150, "summer"))