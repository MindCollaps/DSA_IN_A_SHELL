from enum import Enum

from game.LeitEigenschaft import LeitEigenschaft

def get_kampftechnik_wert(player, kampftechnik) -> int:
    return player[kampftechnik.value-1][1]

def set_kampftechnik_wert(player, kampftechnik, value: int):
    player.kampftechnik[kampftechnik.value-1] = (kampftechnik, value)

class Kampftechnik(Enum):
    Armbrueste = (0, LeitEigenschaft.FF)
    Boegen = (1, LeitEigenschaft.FF)
    Dolche = (2, LeitEigenschaft.GE)
    Fechtwaffen = (3, LeitEigenschaft.GE)
    Hiebwaffen = (4, LeitEigenschaft.KK)
    Kettenwaffen = (5, LeitEigenschaft.KK)
    Lanzen = (6, LeitEigenschaft.KK)
    RAUFEN = (8, LeitEigenschaft.KK)
    Schilde = (9, LeitEigenschaft.KK)
    Schwerter = (10, LeitEigenschaft.GE)
    Stangenwaffen = (11, LeitEigenschaft.GE)
    Wurfwaffen = (12, LeitEigenschaft.FF)
    Zweihandhiebwaffen = (13, LeitEigenschaft.KK)
    Zweihandschwerter = (14, LeitEigenschaft.KK)

    def __init__(self, id, leiteigenschaft: LeitEigenschaft):
        self.id = id
        self.leiteigenschaft: LeitEigenschaft = leiteigenschaft