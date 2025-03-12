import random

from game import Player
from game.Character import Spezies
from item import Item
from item.weapon.Fist import Fist
from npc.DroppingNpc import DroppingNpc
from npc.Enemy import Enemy


class MeatBag(Enemy, DroppingNpc):
    def __init__(self):
        super().__init__("A weird looking Meat Bag", [Fist()], Spezies.KleinerGegner)
        self.xp_reward = 100

    def attack(self, player: Player) -> int:
        return random.randint(1, 5)

    def get_drops(self) -> list[Item]:
        return []
