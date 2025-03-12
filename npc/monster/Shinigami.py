import random

from game import Player
from game.Character import Spezies
from item import Item
from item.weapon.Fist import Fist
from npc.DroppingNpc import DroppingNpc
from npc.Enemy import Enemy


class Shinigami(Enemy, DroppingNpc):
    def __init__(self):
        super().__init__("Shinigami", [Fist()], Spezies.KleinerGegner)
        self.xp_reward = 100

    def attack(self, player: Player) -> int:
        return random.randint(5, 8)

    def get_drops(self) -> list[Item]:
        return []
