import random

from game import Player
from item import Item
from npc import DroppingNpc
from npc import Enemy


class NoFace(Enemy, DroppingNpc):
    def __init__(self):
        super().__init__("No-Face", [], 15, 15)

    def attack(self, player: Player) -> int:
        return random.randint(3, 5)

    def get_drops(self) -> list[Item]:
        return []
