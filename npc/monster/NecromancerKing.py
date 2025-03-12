import random

from game import Player
from game.Character import Spezies
from item import Item
from item.weapon.Fist import Fist
from npc.DroppingNpc import DroppingNpc
from npc.Enemy import Enemy


class NecromancerKing(Enemy, DroppingNpc):
    def __init__(self):
        super().__init__("Xaran the Necromancer King", [Fist()], Spezies.KleinerGegner)
        self.xp_reward = 100

    def attack(self, player: Player) -> int:
        return random.randint(5, 13)

    def get_drops(self) -> list[Item]:
        return []
