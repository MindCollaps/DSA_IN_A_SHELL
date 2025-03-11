from game.Kampftechnik import Kampftechnik
from item.Rarity import Rarity
from item.weapon.Weapon import Weapon
from utils.dice.Dices import Dice

class RareScythe(Weapon):
    def __init__(self):
        super().__init__(
            name="Reaper's Scythe",
            description="Schnitterklinge mit Knochengriff",
            price=250,
            rarity=Rarity.RARE,
            kampftechnik=Kampftechnik.Stangenwaffen,
            tp=1 * Dice(8),
            at_bonus=3
        )