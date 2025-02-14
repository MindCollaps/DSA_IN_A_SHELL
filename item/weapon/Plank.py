from game import Player
from game.Kampftechnik import Kampftechnik
from item import Rarity
from item import Weapon
from npc import Enemy
from utils.dice.Dices import Dice


class Plank(Weapon):
    def __init__(self):
        super().__init__("Plank", "A peace of wood", 100, Rarity.COMMON, Kampftechnik.RAUFEN, 1 * Dice(6))
