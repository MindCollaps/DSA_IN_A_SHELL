import random
from typing import override, overload

from npc import DroppingNpc
from npc import Enemy
from game import Player
from item import Item

class Slime(Enemy, DroppingNpc):
    def __init__(self):
        super().__init__("Slime", [], 15, 15)


    def attack(self, player: Player) -> int:
        return random.randint(3, 6)

    def get_drops(self) -> list[Item]:
        return []