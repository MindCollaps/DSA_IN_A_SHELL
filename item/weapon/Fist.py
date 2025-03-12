from game.Kampftechnik import Kampftechnik
from item.Rarity import Rarity
from item.weapon.Weapon import Weapon
from utils.dice.Dices import Dice


class Fist(Weapon):
    def __init__(self):
        super().__init__(
            name="Fist",
            description="Naturliche Nahkampfwaffe",
            price=0,
            rarity=Rarity.COMMON,
            kampftechnik=Kampftechnik.RAUFEN,
            tp=1 * Dice(3),  # Wichtig: 1* für Dices-Objekt
            at_bonus=0
        )
