from game.LeitEigenschaft import LeitEigenschaft, get_leiteigenschaft
from game.Geldbeutel import Geldbeutel
from game.Kampftechnik import Kampftechnik
from enum import Enum

class Spezies(Enum):
    Mensch = 0
    Elf = 1
    Zwerg = 2

class Character:
    def __init__(self, name: str, hp_grundwert: int=12, zk_grundwert: int=12):
        self.name: str = name
        self.spezies: Spezies = Spezies.Mensch
        self.kampftechnik = [(kt, 8) for kt in Kampftechnik]
        self.leit_eigenschaft = [(le, 8) for le in LeitEigenschaft]

        self.hp: int = hp_grundwert + get_leiteigenschaft(self, LeitEigenschaft.KO) + get_leiteigenschaft(self, LeitEigenschaft.KO)
        self.zk: int = zk_grundwert + int(get_leiteigenschaft(self, LeitEigenschaft.KO) + get_leiteigenschaft(self, LeitEigenschaft.KO) + get_leiteigenschaft(self, LeitEigenschaft.KK) / 6)
        self.aw: int = int(get_leiteigenschaft(self, LeitEigenschaft.GE) / 2)
        self.geldbeutel: Geldbeutel = Geldbeutel()
