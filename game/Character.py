from enum import Enum, auto

from game.Geldbeutel import Geldbeutel
from game.Kampftechnik import Kampftechnik
from game.LeitEigenschaft import LeitEigenschaft, get_leiteigenschaft
from item.armor.Armor import Armor
from game.leveling_system import LevelSystem

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
        self.kampftechnik = [(kt, 8) for kt in Kampftechnik]


class Character:
    def __init__(self, name: str, spezies: Spezies):
        self.name: str = name
        self.spezies: Spezies = spezies
        self.kampftechnik = [(kt, 8) for kt in Kampftechnik]
        self.leit_eigenschaft = [(le, 8) for le in LeitEigenschaft]
        self.ruestung: Armor | None = None
        self.current_hp = self.base_hp  # Wird durch @property aktualisiert
        self.geldbeutel = Geldbeutel()
        self.geldbeutel.kreuzer = 50  # Startkapital hinzufügen

    @property
    def base_hp(self) -> int:
        ko_wert = next(wert for le, wert in self.leit_eigenschaft if le == LeitEigenschaft.KO)
        return self.spezies.hp_gw + 2 * ko_wert

    @property
    def zk(self) -> int:
        ko_wert = next(wert for le, wert in self.leit_eigenschaft if le == LeitEigenschaft.KO)
        kk_wert = next(wert for le, wert in self.leit_eigenschaft if le == LeitEigenschaft.ST)  # Annahme: KK = ST
        return self.spezies.zk_gw + int(ko_wert + kk_wert / 6)

    @property
    def aw(self) -> int:
        ge_wert = next(wert for le, wert in self.leit_eigenschaft if le == LeitEigenschaft.GE)
        return int(ge_wert / 2)

    def kampftechnik_wert(self, kampftechnik: Kampftechnik) -> int:
        """Gibt den Kampftechnik-Wert zurück"""
        return next(wert for kt, wert in self.kampftechnik if kt == kampftechnik)