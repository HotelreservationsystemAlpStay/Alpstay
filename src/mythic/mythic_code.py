from PIL import Image
import random

class Mythic:
    @staticmethod
    def wtf():
        number = random.randint(0, 1)
        if number == 0:
            path = "src/mythic/very_mythic.png"
        elif number == 1:
            path = "src/mythic/very_mythic_1.png"
        image = Image.open(path)
        image.show()
