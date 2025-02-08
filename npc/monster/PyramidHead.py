import random

from game import Player
from item import Item
from npc import DroppingNpc
from npc import Enemy


class PyramidHead(Enemy, DroppingNpc):
    def __init__(self):
        super().__init__("The Pyramidhead", [], 85, 85)

    def attack(self, player: Player) -> int:
        return random.randint(7, 14)

    def get_drops(self) -> list[Item]:
        return []
