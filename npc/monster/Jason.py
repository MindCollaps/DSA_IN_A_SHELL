from game.Character import Spezies
from item import Item
from item.weapon.Fist import Fist
from npc.DroppingNpc import DroppingNpc
from npc.Enemy import Enemy


class Jason(Enemy, DroppingNpc):
    def __init__(self):
        super().__init__("Jason", [Fist()], Spezies.KleinerGegner)
        self.xp_reward = 100

    def get_drops(self) -> list[Item]:
        return []
