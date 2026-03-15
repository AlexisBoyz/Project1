from enum import Enum

class Operator(Enum):
    MTS = "МТС"
    Beline = "Билайн"
    Megafon = "Мегафон"
    Tele2 = "Теле2"

    def __str__(self):
        return self.value