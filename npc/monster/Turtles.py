import random
from game.Character import Spezies
from game import Player
from item import Item
from npc.DroppingNpc import DroppingNpc
from npc.Enemy import Enemy
from item.weapon.Fist import Fist


class Turtles(Enemy, DroppingNpc):
    def __init__(self):
        super().__init__("The Teenage Mutant Ninja Turtles", [Fist()], Spezies.KleinerGegner)

    def attack(self, player: Player) -> int:
        return random.randint(7, 13)

    def get_drops(self) -> list[Item]:
        return []
