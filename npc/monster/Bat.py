import random

from npc import DroppingNpc
from npc import Enemy
from game import Player

class Bat(Enemy, DroppingNpc):
    def __init__(self):
        super().__init__("Bat", [], 10, 10)

    def attack(self, player: Player) -> int:
        return random.randint(1, 5)

    def get_drops(self):
        return []