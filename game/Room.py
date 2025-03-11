from enum import Enum
import random
from item.Rarity import Rarity
from game.Random import getRandomItems, getRandomEnemy, get_random_rarity

class RoomType(Enum):
    EMPTY = 0
    MONSTER = 1
    ITEM = 2
    BOSS = 3
    SHOP = 4

class Room:
    def __init__(self, dungeon):
        self.description: str = ""
        self.items: list = []
        self.monster = None
        self.walls: list = []
        self.dungeon = dungeon
        self.Room_Type: RoomType = RoomType.EMPTY
        self.generate_room()

    def generate_room(self):
        room_type_probabilities = {
            RoomType.EMPTY: 0.35,
            RoomType.ITEM: 0.2,
            RoomType.BOSS: 0.1,
            RoomType.MONSTER: 0.3,
            RoomType.SHOP: 0.05
        }

        self.Room_Type = random.choices(
            list(room_type_probabilities.keys()),
            weights=list(room_type_probabilities.values()),
            k=1
        )[0]

        if self.Room_Type == RoomType.EMPTY:
            self.description = "Ein leerer Raum. Hier gibt es nichts Besonderes."

        elif self.Room_Type == RoomType.MONSTER:
            rarity = get_random_rarity()
            self.monster = getRandomEnemy(rarity)
            self.description = f"Ein düsterer Raum. {self.monster.name} lauert in der Ecke!" if self.monster else "Ein seltsamer Raum. Etwas scheint nicht zu stimmen."

        elif self.Room_Type == RoomType.ITEM:
            rarity = get_random_rarity()
            items = getRandomItems(rarity, 1)
            self.items.extend(items)
            self.description = "Ein Raum mit einer Schatztruhe. Vielleicht ist etwas Nützliches darin." if items else "Ein Raum mit einer leeren Schatztruhe. Nichts Interessantes hier."