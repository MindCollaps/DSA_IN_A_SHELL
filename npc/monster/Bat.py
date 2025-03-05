from game.Character import Spezies
from item.weapon.Fist import Fist
from npc import DroppingNpc
from npc import Enemy


class Bat(Enemy, DroppingNpc):
    def __init__(self):
        super().__init__("Bat", Fist(), Spezies.KleinerGegner) #Todo make claws?

    def get_drops(self) -> list[object]:
        return []
