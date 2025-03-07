import random
from typing import List
import sys

from item.weapon.BasicSword import BasicSword
from item.weapon.BasicBow import BasicBow
from item.weapon.BasicDagger import BasicDagger
from item.weapon.EpicBow import EpicBow
from item.weapon.EpicKatana import EpicKatana
from item.weapon.LegendarySword import LegendarySword
from item.weapon.Plank import Plank
from item.weapon.RareScythe import RareScythe
from item.weapon.RareSword import RareSword
from item.weapon.RareWand import RareWand
from item.weapon.Shovel import Shovel
from item.weapon.SoapSock import SoapSock
from item.weapon.Stones import Stones
from item.weapon.Warhammer import Warhammer

from npc.Enemy import Enemy
from npc.monster.Bat import Bat
from npc.monster.FreddyBear import FreddyBear
from npc.monster.Jason import Jason
from npc.monster.Korosensei import Korosensei
from npc.monster.MeatBag import MeatBag
from npc.monster.NecromancerKing import NecromancerKing
from npc.monster.NoFace import NoFace
from npc.monster.PyramidHead import PyramidHead
from npc.monster.Shinigami import Shinigami
from npc.monster.Slime import Slime
from npc.monster.Turtles import Turtles
from npc.monster.ZombieChicken import ZombieChicken

from item.Item import Item
from item.Rarity import Rarity

from item.usable.HealthPotion import HealthPotion
from item.usable.Stick import Stick
from item.usable.Beer import Beer
from item.usable.Bottle import Bottle
from item.usable.Curry import Curry
from item.usable.Fruit import Fruit
from item.usable.GoldenApple import GoldenApple
from item.usable.HotCurry import HotCurry
from item.usable.Jar import Jar
from item.usable.Mask import Mask
from item.usable.Stone import Stone
from item.usable.StrengthPotion import StrengthPotion
from item.usable.ShinyBottle import ShinyBottle



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
    ItemPossibility(StrengthPotion("Normal Strength Potion", "A normal strength Potion :D", 5, Rarity.COMMON, 4), Rarity.COMMON),
    ItemPossibility(StrengthPotion("The Knights strength", "It gives you the Strengths of a knight", 15, Rarity.RARE, 10), Rarity.RARE),
    ItemPossibility(Stick(), Rarity.COMMON),
    ItemPossibility(Beer(), Rarity.COMMON),
    ItemPossibility(Bottle(), Rarity.COMMON),
    ItemPossibility(Curry(), Rarity.COMMON),
    ItemPossibility(Fruit(), Rarity.COMMON),
    ItemPossibility(GoldenApple(), Rarity.RARE),
    ItemPossibility(HotCurry(), Rarity.COMMON),
    ItemPossibility(Jar(), Rarity.RARE),
    ItemPossibility(Mask(), Rarity.RARE),
    ItemPossibility(ShinyBottle(), Rarity.EPIC),
    ItemPossibility(Stone(), Rarity.COMMON)
]

monsters = [
    MonsterPossibility(Bat(), Rarity.COMMON),
    MonsterPossibility(FreddyBear(), Rarity.COMMON),
    MonsterPossibility(Jason(), Rarity.RARE),
    MonsterPossibility(Korosensei(), Rarity.RARE),
    MonsterPossibility(MeatBag(), Rarity.COMMON),
    MonsterPossibility(NecromancerKing(), Rarity.LEGENDARY),
    MonsterPossibility(NoFace(), Rarity.EPIC),
    MonsterPossibility(PyramidHead(), Rarity.EPIC),
    MonsterPossibility(Shinigami(), Rarity.RARE),
    MonsterPossibility(Slime(), Rarity.COMMON),
    MonsterPossibility(Turtles(), Rarity.RARE),
    MonsterPossibility(ZombieChicken(), Rarity.COMMON)
]

weapons = [
    ItemPossibility(BasicSword(), Rarity.COMMON),
    ItemPossibility(BasicBow(),Rarity.COMMON),
    ItemPossibility(BasicDagger(), Rarity.COMMON),
    ItemPossibility(EpicBow(), Rarity.EPIC),
    ItemPossibility(EpicKatana(), Rarity.EPIC),
    ItemPossibility(LegendarySword(), Rarity.LEGENDARY),
    ItemPossibility(Plank(), Rarity.COMMON),
    ItemPossibility(RareScythe(), Rarity.RARE),
    ItemPossibility(RareSword(), Rarity.RARE),
    ItemPossibility(RareWand(), Rarity.RARE),
    ItemPossibility(Shovel(), Rarity.COMMON),
    ItemPossibility(SoapSock(), Rarity.COMMON),
    ItemPossibility(Stones(), Rarity.COMMON),
    ItemPossibility(Warhammer(), Rarity.EPIC)
]

def getRandomItems(rarity: Rarity, amount: int, self) -> List[Item]:
        ItemPossibility = {
        Rarity.COMMON: 0.8,
        Rarity.RARE: 0.6,
        Rarity.EPIC: 0.4,
        Rarity.LEGENDARY: 0.2
        }

        if random.random() <= ItemPossibility[rarity]:
            items_of_rarity = [item for item in self.items if item.rarity == rarity]
        if items_of_rarity:
            return random.choice(items_of_rarity)

        return None

def getRandomEnemy(rarity: Rarity, self) -> Enemy:
        EnemyPossibility = {
            Rarity.COMMON: 0.8,
            Rarity.RARE: 0.6,
            Rarity.EPIC: 0.4,
            Rarity.LEGENDARY: 0.2
            }
        
        if random.random() <= EnemyPossibility[rarity]:
            enemy_of_rarity = [item for item in self.items if item.rarity == rarity]
        if enemy_of_rarity:
            return random.choice(enemy_of_rarity)

        return None