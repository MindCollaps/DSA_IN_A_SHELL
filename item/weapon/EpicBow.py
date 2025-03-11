from game.Kampftechnik import Kampftechnik
from item.Rarity import Rarity
from item.weapon.Weapon import Weapon
from utils.dice.Dices import Dice

class EpicBow(Weapon):
    def __init__(self):
        super().__init__(
            name="Epic Bow",
            description="Ein magischer Bogen mit Elfenbein-Verzierungen",
            price=350,
            rarity=Rarity.EPIC,
            kampftechnik=Kampftechnik.Boegen,
            tp=2 * Dice(8),
            at_bonus=4
        )