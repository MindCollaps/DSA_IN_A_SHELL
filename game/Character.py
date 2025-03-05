from enum import Enum, auto

from game.Geldbeutel import Geldbeutel
from game.Kampftechnik import Kampftechnik
from game.LeitEigenschaft import LeitEigenschaft, get_leiteigenschaft
from item.armor.Armor import Armor


class Spezies(Enum):
    Mensch = (auto(), 5, -5, 8)  # HP_GW, ZK_GW, GW
    Elf = (auto(), 2, -6, 8)
    HalbElf = (auto(), 5, -6, 8)
    Zwerg = (auto(), 8, -4, 6)
    KleinerGegner = (auto(), 3, -5, 8)


    def __init__(self, id, hp_gw: int, zk_gw: int, gs_gw: int):
        self.id = id
        self.hp_gw = hp_gw
        self.zk_gw = zk_gw
        self.gs_gw = gs_gw


class Character:
    def __init__(self, name: str, spezies: Spezies):
        self.name: str = name
        self.spezies: Spezies = spezies
        self.kampftechnik = [(kt, 8) for kt in Kampftechnik]
        self.leit_eigenschaft = [(le, 8) for le in LeitEigenschaft]
        self.ruestung: Armor | None = None

        self.base_hp: int = self.spezies.hp_gw + get_leiteigenschaft(self, LeitEigenschaft.KO) + get_leiteigenschaft(
            self, LeitEigenschaft.KO)
        self.zk: int = self.spezies.zk_gw + int(
            get_leiteigenschaft(self, LeitEigenschaft.KO) + get_leiteigenschaft(self,
                                                                                LeitEigenschaft.KO) + get_leiteigenschaft(
                self, LeitEigenschaft.KK) / 6)
        self.aw: int = int(get_leiteigenschaft(self, LeitEigenschaft.GE) / 2)
        self.current_hp = self.base_hp
