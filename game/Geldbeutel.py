from enum import  Enum

class GeldType(Enum):
    KREUZER = 0
    HELLER = 1
    SILBERTALER = 2
    DUKATEN = 3

class Geldbeutel:
    def __init__(self):
        self.dukaten = 0
        self.silbertaler = 0
        self.heller = 0
        self.kreuzer = 0