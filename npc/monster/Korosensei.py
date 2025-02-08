import random

from game import Player
from item import Item
from npc import DroppingNpc
from npc import Enemy


class Korosensei(Enemy, DroppingNpc):
    def __init__(self):
        super().__init__("Koro-Sensei", [], 60, 60)

    def attack(self, player: Player) -> int:
        return random.randint(6, 10)

    def get_drops(self) -> list[Item]:
        return []
