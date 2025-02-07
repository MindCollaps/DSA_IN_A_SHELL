import random
from typing import override, overload

from npc import DroppingNpc
from npc import Enemy
from game import Player
from item import Item

class Jason(Enemy, DroppingNpc):
    def __init__(self):
        super().__init__("Jason", [], 35, 35)


    def attack(self, player: Player) -> int:
        return random.randint(3, 8)

    def get_drops(self) -> list[Item]:
        return []