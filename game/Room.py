from enum import Enum
import random
from item.Rarity import Rarity
from game.Random import getRandomItems, getRandomEnemy, get_random_rarity
from item.Item import Item

class RoomType(Enum):
    EMPTY = 0
    MONSTER = 1
    ITEM = 2
    BOSS = 3


class Room:
    def __init__(self, dungeon):
        from npc import Enemy
        from item import Item

        self.description: str = ""
        self.items: list[Item] = []
        self.monster: Enemy = None
        self.walls: list[tuple[int, int]] = []
        self.dungeon = dungeon
        self.Room_Type: RoomType = RoomType.EMPTY
        self.generate_room()

    def generate_room(self):
        room_type_probabilities = {
        RoomType.EMPTY: 0.4,
        RoomType.ITEM: 0.2,
        RoomType.BOSS: 0.1,
        RoomType.MONSTER: 0.3
        }

        self.Room_Type = random.choices(list(room_type_probabilities.keys()),
                weights=list(room_type_probabilities.values()))[0]

        if self.Room_Type == RoomType.EMPTY:
            self.description = "Ein leerer Raum. Hier gibt es nichts Besonderes."
        

        elif self.Room_Type == RoomType.MONSTER:
            rarity = get_random_rarity()
            self.monster = getRandomEnemy(rarity, self)
            if self.monster:
                self.description = f"Ein düsterer Raum. {self.monster.name} lauert in der Ecke!"

            else:
                self.description = "Ein seltsamer Raum. Etwas scheint nicht zu stimmen."


        elif self.Room_Type == RoomType.ITEM:
            rarity = get_random_rarity()
            item = getRandomItems(rarity, 1, self)
            if item:
                self.items.extend(item)
                self.description = "Ein Raum mit einer Schatztruhe. Vielleicht ist etwas Nützliches darin."

            else:
                self.description = "Ein Raum mit einer leeren Schatztruhe. Nichts Interessantes hier."