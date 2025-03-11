from game.Character import Spezies
from item.weapon.Fist import Fist
from npc.DroppingNpc import DroppingNpc
from npc.Enemy import Enemy


class Bat(Enemy, DroppingNpc):
    def __init__(self):
        super().__init__("Bat", [Fist()], Spezies.KleinerGegner) #Todo make claws?
        self.xp_reward = 100

    def get_drops(self) -> list[object]:
        return []
