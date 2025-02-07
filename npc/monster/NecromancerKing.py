import random
from typing import override, overload

from npc import DroppingNpc
from npc import Enemy
from game import Player
from item import Item

class NecromancerKing(Enemy, DroppingNpc):
    def __init__(self):
        super().__init__("Xaran the Necromancer King", [], 120, 120)


    def attack(self, player: Player) -> int:
        return random.randint(5, 13)

    def get_drops(self) -> list[Item]:
        return []