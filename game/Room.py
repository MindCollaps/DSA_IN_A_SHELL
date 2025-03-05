from enum import Enum
from npc import monster
from item import Item


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
    room_type_probabilities = {
        RoomType.EMPTY = 0.4,
        RoomType.ITEM = 0.2,
        RoomType.BOSS = 0.1,
        RoomType.MONSTER = 0.3
    }

self.Room_Type = random.choices(list(room_type_probabilities.keys()),
            weights=list(room_type_probabilities.values()))[0]

if self.Room_Type == RoomType.EMPTY:
            self.description = "Ein leerer Raum. Hier gibt es nichts Besonderes."
            self.monsters.append("")  # Leerer String für Räume ohne Monster

elif self.Room_Type == RoomType.MONSTER:
            monster = self.select_monster_by_rarity()
            self.monsters.append(monster)
            self.description = f"Ein düsterer Raum. {monster.name} lauert in der Ecke!"

elif self.Room_Type == RoomType.ITEM:
            item = getRandomItems(rarity: Rarity): Item[]
            self.items.append(item)
            self.description = f"Ein Raum mit einem Schatz! Du findest {item.name}."
            self.monsters.append("")
