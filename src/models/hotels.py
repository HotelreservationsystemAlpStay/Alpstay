class Hotel:
    def __init__(self, hotel_id: int, name: str, stars: int):
        self._hotel_id = hotel_id
        self._name = name
        self._stars = stars
    @property
    def hotel_id(self):
        return self._hotel_id
    @hotel_id.setter
    def hotel_id(self, new_hotel_id):
        self._hotel_id = new_hotel_id
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, new_name):
        self._name = new_name
    @property
    def stars(self):
        return self._stars
    @stars.setter
    def stars(self, new_stars):
        self._stars = new_stars