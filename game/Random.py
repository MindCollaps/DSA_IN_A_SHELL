import random
from typing import List
import sys

from item.usable.HealthPotion import HealthPotion
from item.weapon.BasicSword import BasicSword
from npc.Enemy import Enemy
from npc.monster.Bat import Bat
from item.Item import Item
from item.Rarity import Rarity
from item.usable.Stick import Stick

class ItemPossibility:
    def __init__(self, item: Item, rarity: Rarity):
        self.item = item
        self.rarity = rarity

class MonsterPossibility:
    def __init__(self, monster: Enemy, rarity: Rarity):
        self.monster = monster
        self.rarity = rarity

items = [
    ItemPossibility(HealthPotion("Normal Health Potion", "A normal health Potion :D", 5, Rarity.COMMON, 4), Rarity.COMMON),
    ItemPossibility(HealthPotion("Supi dupi", "Crazy Health lol", 50, Rarity.LEGENDARY, 40), Rarity.LEGENDARY),
    ItemPossibility(Stick(), Rarity.COMMON),
]

monsters = [
    MonsterPossibility(Bat(), Rarity.COMMON),
]

weapons = [
    ItemPossibility(BasicSword(), Rarity.COMMON),
]

def getRandomItems(rarity: Rarity, amount: int) -> List[Item]:
    # will do later
    pass

def getRandomEnemy() -> Enemy:
    return Bat()