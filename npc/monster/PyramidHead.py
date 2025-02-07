import random
from typing import override, overload

from npc import DroppingNpc
from npc import Enemy
from game import Player
from item import Item

class PyramidHead(Enemy, DroppingNpc):
    def __init__(self):
        super().__init__("The Pyramidhead", [], 85, 85)


    def attack(self, player: Player) -> int:
        return random.randint(7, 14)

    def get_drops(self) -> list[Item]:
        return []