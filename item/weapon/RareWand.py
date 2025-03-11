from game.Kampftechnik import Kampftechnik
from item.Rarity import Rarity
from item.weapon.Weapon import Weapon
from utils.dice.Dices import Dice

class RareWand(Weapon):
    def __init__(self):
        super().__init__(
            name="Arcane Wand",
            description="Eichenholzstab mit Kristallspitze",
            price=150,
            rarity=Rarity.RARE,
            kampftechnik=Kampftechnik.Wurfwaffen,
            tp=1 * Dice(6),
            at_bonus=2
        )