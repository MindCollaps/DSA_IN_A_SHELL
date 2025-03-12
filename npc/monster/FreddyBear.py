import random

from game import Player
from game.Character import Spezies
from item import Item
from item.weapon.Fist import Fist
from npc.DroppingNpc import DroppingNpc
from npc.Enemy import Enemy


class FreddyBear(Enemy, DroppingNpc):
    def __init__(self):
        super().__init__("Freddy Baer", [Fist()], Spezies.KleinerGegner)
        self.xp_reward = 100

    def attack(self, player: Player) -> int:
        return random.randint(6, 8)

    def get_drops(self) -> list[Item]:
        return []
