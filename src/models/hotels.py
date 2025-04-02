#Achtung z. B. hotel_id: int würde keinen Value Error raisen wenn man String gibt, dafür braucht es Code
class Hotel:
    def __init__(self, hotel_id: int, name: str, stars: int):
        if not isinstance(hotel_id, int):
            raise ValueError("Die Hotel Id muss eine Integer sein")
        if not isinstance(name, str):
            raise ValueError("Der Hotelname muss ein String sein")
        if not isinstance(stars, int):
            raise ValueError("Die Sterne des Hotels müssen eine Integer sein")
        if name.strip() == "":
            raise ValueError("Bitte gib einen Hotelnamen ein")
        if hotel_id <1:
            raise ValueError("Die Hotel ID darf nicht negativ sein")
        if stars >5 or stars <1:
            raise ValueError("Die Sterne des Hotel müssen zwischen 1 und 5 liegen")
        self._hotel_id = hotel_id
        self._name = name
        self._stars = stars
    @property
    def hotel_id(self):
        return self._hotel_id
    @hotel_id.setter
    def hotel_id(self, new_hotel_id: int):
        if not isinstance(new_hotel_id, int):
            raise ValueError("Die neue Hotel ID muss eine Integer sein")
        if new_hotel_id <1:
            raise ValueError("Die neue Hotel ID darf nicht negativ sein")
        self._hotel_id = new_hotel_id
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, new_name: str):
        if not isinstance(new_name, str):
            raise ValueError("Der neue Hotelname muss ein String sein")
        if new_name.strip() == "":
            raise ValueError("Bitte gib den neuen Hotelnamen ein")
        self._name = new_name
    @property
    def stars(self):
        return self._stars
    @stars.setter
    def stars(self, new_stars: int):
        if not isinstance(new_stars, int):
            raise ValueError("Die neuen Sterne des Hotels müssen eine Integer sein")
        if new_stars >5 or new_stars <1:
            raise ValueError("Die neuen Sterne des Hotel müssen zwischen 1 und 5 liegen")
        self._stars = new_stars
    def __str__(self):
        return f"Hotel {self._name} hat {self._stars} Sterne und {self._hotel_id} als Hotel ID"