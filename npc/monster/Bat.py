import random

from npc import DroppingNpc
from npc import Enemy


class Bat(Enemy, DroppingNpc):
    def __init__(self):
        super().__init__("Bat", 10, 10)

    def attack(self, player) -> int:
        return random.randint(1, 5)

    def get_drops(self) -> list[object]:
        return []
