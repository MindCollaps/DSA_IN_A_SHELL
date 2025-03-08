import random
from game.Character import Spezies
from game import Player
from item import Item
from npc.DroppingNpc import DroppingNpc
from npc.Enemy import Enemy
from item.weapon.Fist import Fist


class NecromancerKing(Enemy, DroppingNpc):
    def __init__(self):
        super().__init__("Xaran the Necromancer King", [Fist()], Spezies.KleinerGegner)

    def attack(self, player: Player) -> int:
        return random.randint(5, 13)

    def get_drops(self) -> list[Item]:
        return []
