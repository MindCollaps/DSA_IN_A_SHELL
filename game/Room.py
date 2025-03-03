from enum import Enum


class RoomType(Enum):
    EMPTY = 0
    MONSTER = 1
    ITEM = 2
    BOSS = 3


class Room:
    def __init__(self, dungeon):
        from game import Dungeon
        from npc import Enemy
        from item import Item

        self.description: str = ""
        self.items: list[Item] = []
        self.monsters: list[Enemy] = []
        self.walls: list[tuple[int, int]] = []
        self.dungeon: Dungeon = dungeon
        self.Room_Type: RoomType = RoomType.EMPTY
        self.generate_room()

    def generate_room(self):
        self.monsters.append("")
