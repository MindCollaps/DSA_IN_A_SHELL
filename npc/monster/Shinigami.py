import random
from game.Character import Spezies
from game import Player
from item import Item
from npc.DroppingNpc import DroppingNpc
from npc.Enemy import Enemy
from item.weapon.Fist import Fist


class Shinigami(Enemy, DroppingNpc):
    def __init__(self):
        super().__init__("Shinigami", [Fist()], Spezies.KleinerGegner)
        self.xp_reward = 100

    def attack(self, player: Player) -> int:
        return random.randint(5, 8)

    def get_drops(self) -> list[Item]:
        return []
