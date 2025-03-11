from game.Kampftechnik import Kampftechnik
from item.Rarity import Rarity
from item.weapon.Weapon import Weapon
from utils.dice.Dices import Dice

class SoapSock(Weapon):
    def __init__(self):
        super().__init__(
            name="Soap Sock",
            description="Seifenstück in einem Socken",
            price=1,
            rarity=Rarity.COMMON,
            kampftechnik=Kampftechnik.RAUFEN,
            tp=1 * Dice(4),
            at_bonus=0
        )