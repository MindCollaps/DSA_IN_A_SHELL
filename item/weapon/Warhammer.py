from game.Kampftechnik import Kampftechnik
from item.Rarity import Rarity
from item.weapon.Weapon import Weapon
from utils.dice.Dices import Dice

class Warhammer(Weapon):
    def __init__(self):
        super().__init__(
            name="Warhammer",
            description="Schwerer Zweihandhammer",
            price=120,
            rarity=Rarity.RARE,
            kampftechnik=Kampftechnik.Zweihandhiebwaffen,
            tp=Dice(10) + 2,
            at_bonus=2,
            pa_bonus=-2
        )