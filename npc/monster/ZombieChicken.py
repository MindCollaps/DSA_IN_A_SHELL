import random

from game import Player
from item import Item
from npc import DroppingNpc
from npc import Enemy


class ZombieChicken(Enemy, DroppingNpc):
    def __init__(self):
        super().__init__("Zombie Chicken", [], 10, 10)

    def attack(self, player: Player) -> int:
        return random.randint(2, 6)

    def get_drops(self) -> list[Item]:
        return []
