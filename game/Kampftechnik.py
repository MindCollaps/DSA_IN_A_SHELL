from enum import Enum

from game.LeitEigenschaft import LeitEigenschaft


class Kampftechnik(Enum):
    # Korrekte Referenzierung der LeitEigenschaft-Enum-Member
    Armbrueste = (1, LeitEigenschaft.FF)
    Boegen = (2, LeitEigenschaft.FF)
    Dolche = (3, LeitEigenschaft.GE)
    Fechtwaffen = (4, LeitEigenschaft.GE)
    Hiebwaffen = (5, LeitEigenschaft.KK)
    Kettenwaffen = (6, LeitEigenschaft.KK)
    Lanzen = (7, LeitEigenschaft.KK)
    RAUFEN = (8, LeitEigenschaft.KK)
    Schilde = (9, LeitEigenschaft.KK)
    Schwerter = (10, LeitEigenschaft.GE)
    Stangenwaffen = (11, LeitEigenschaft.GE)
    Wurfwaffen = (12, LeitEigenschaft.FF)
    Zweihandhiebwaffen = (13, LeitEigenschaft.KK)
    Zweihandschwerter = (14, LeitEigenschaft.KK)

    def __init__(self, id, leiteigenschaft: LeitEigenschaft):
        self.id = id
        self.leiteigenschaft = leiteigenschaft
