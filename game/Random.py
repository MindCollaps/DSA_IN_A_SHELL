import random
from typing import List
from item.Rarity import Rarity
from item.Item import Item
from npc.Enemy import Enemy

# --- Waffen ---
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

# --- Monster ---
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

# --- Items & Usables ---
from item.usable.HealthPotion import HealthPotion
from item.usable.StrengthPotion import StrengthPotion
from item.usable.Stick import Stick
from item.usable.Beer import Beer
from item.usable.Bottle import Bottle
from item.usable.Curry import Curry
from item.usable.Fruit import Fruit
from item.usable.GoldenApple import GoldenApple
from item.usable.HotCurry import HotCurry
from item.usable.Jar import Jar
from item.usable.Mask import Mask
from item.usable.ShinyBottle import ShinyBottle
from item.usable.Stone import Stone

class ItemPossibility:
    def __init__(self, item: Item, rarity: Rarity):
        self.item = item
        self.rarity = rarity

class MonsterPossibility:
    def __init__(self, monster: Enemy, rarity: Rarity):
        self.monster = monster
        self.rarity = rarity

# --- Vollständige Items ---
items = [
    # Health Potions
    ItemPossibility(
        HealthPotion(
            name="Kleiner Heiltrank",
            description="Stellt 20 HP wieder her",
            price=25,
            rarity=Rarity.COMMON,
            heal_amount=20
        ),
        Rarity.COMMON
    ),
    ItemPossibility(
        HealthPotion(
            name="Großer Heiltrank",
            description="Stellt 50 HP wieder her",
            price=60,
            rarity=Rarity.RARE,
            heal_amount=50
        ),
        Rarity.RARE
    ),

    # Strength Potions
    ItemPossibility(
        StrengthPotion(
            name="Stärketrank",
            description="+2 Stärke für 10 Minuten",
            price=40,
            rarity=Rarity.COMMON,
            strength_amount=2
        ),
        Rarity.COMMON
    ),
    ItemPossibility(
        StrengthPotion(
            name="Mächtiger Stärketrank",
            description="+5 Stärke für 15 Minuten",
            price=100,
            rarity=Rarity.RARE,
            strength_amount=5
        ),
        Rarity.RARE
    ),

    # Andere Items
    ItemPossibility(
        Beer(
            name="Bierkrug",
            description="+1 Mut, -1 Geschick",
            price=15,
            rarity=Rarity.COMMON
        ),
        Rarity.COMMON
    ),
    ItemPossibility(
        GoldenApple(
            name="Goldener Apfel",
            description="Vollständige Heilung",
            price=200,
            rarity=Rarity.LEGENDARY
        ),
        Rarity.LEGENDARY
    ),
    ItemPossibility(
        Stick(
            name="Stock",
            description="Ein einfacher Wanderstock",
            price=5,
            rarity=Rarity.COMMON
        ),
        Rarity.COMMON
    ),
    ItemPossibility(
        Bottle(
            name="Leere Flasche",
            description="Kann mit Flüssigkeiten gefüllt werden",
            price=2,
            rarity=Rarity.COMMON
        ),
        Rarity.COMMON
    ),
    ItemPossibility(
        Curry(
            name="Curry",
            description="Ein mildes Currygericht",
            price=9,
            rarity=Rarity.COMMON
        ),
        Rarity.COMMON
    ),
    ItemPossibility(
        ShinyBottle(
            name="Glitzerflasche",
            description="Enthält mystische Energie",
            price=30,
            rarity=Rarity.EPIC
        ),
        Rarity.EPIC
    )
]

# --- Vollständige Waffen ---
weapons = [
    ItemPossibility(BasicSword(), Rarity.COMMON),
    ItemPossibility(BasicBow(), Rarity.COMMON),
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

# --- Vollständige Monsterliste ---
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

def getRandomItems(rarity: Rarity, amount: int) -> List[Item]:
    items_of_rarity = [ip.item for ip in items if ip.rarity == rarity]
    return random.choices(items_of_rarity, k=amount) if items_of_rarity else []

def getRandomEnemy(rarity: Rarity) -> Enemy:
    enemies_of_rarity = [mp.monster for mp in monsters if mp.rarity == rarity]
    return random.choice(enemies_of_rarity) if enemies_of_rarity else Bat()  # Fallback

def get_random_rarity():
    return random.choices(
        [Rarity.COMMON, Rarity.RARE, Rarity.EPIC, Rarity.LEGENDARY],
        weights=[55, 30, 12, 3],
        k=1
    )[0]