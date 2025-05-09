
    

class RoomAccess():
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