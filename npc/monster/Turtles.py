import random
from typing import override, overload

from npc import DroppingNpc
from npc import Enemy
from game import Player
from item import Item

class Turtles(Enemy, DroppingNpc):
    def __init__(self):
        super().__init__("The Teenage Mutant Ninja Turtles", [], 115, 115)


    def attack(self, player: Player) -> int:
        return random.randint(7, 13)

    def get_drops(self) -> list[Item]:
        return []