import random
from typing import override, overload

from npc import DroppingNpc
from npc import Enemy
from game import Player
from item import Item

class MeatBag(Enemy, DroppingNpc):
    def __init__(self):
        super().__init__("A weird looking Meat Bag", [], 20, 20)


    def attack(self, player: Player) -> int:
        return random.randint(1, 5)

    def get_drops(self) -> list[Item]:
        return []