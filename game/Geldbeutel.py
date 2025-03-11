from enum import Enum


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

    def __str__(self):
        return (
            f"Geldbeutel:\n"
            f"- Dukaten: {self.dukaten}\n"
            f"- Silbertaler: {self.silbertaler}\n"
            f"- Heller: {self.heller}\n"
            f"- Kreuzer: {self.kreuzer}"
        )
