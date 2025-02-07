from enum import Enum

from game import Dungeon
from item import Item
from npc import Enemy


class Room_Type(Enum):
    EMPTY = 0
    MONSTER = 1
    ITEM = 2
    BOSS = 3

class Room:
    def __init__(self, dungeon: Dungeon):
        self.description: str = ""
        self.items: list[Item] = []
        self.monsters: list[Enemy] = []
        self.walls: list[tuple[int, int]] = []
        self.dungeon: Dungeon = dungeon
        self.Room_Type: Room_Type = Room_Type.EMPTY
        self.generate_room()

    def generate_room(self):
        self.monsters.append("")