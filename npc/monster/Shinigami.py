import random
from typing import override, overload

from npc import DroppingNpc
from npc import Enemy
from game import Player
from item import Item

class Shinigami(Enemy, DroppingNpc):
    def __init__(self):
        super().__init__("Shinigami", [], 40, 40)


    def attack(self, player: Player) -> int:
        return random.randint(5, 8)

    def get_drops(self) -> list[Item]:
        return []