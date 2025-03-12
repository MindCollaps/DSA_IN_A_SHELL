from game.Kampftechnik import Kampftechnik
from item.Rarity import Rarity
from item.weapon.Weapon import Weapon
from utils.dice.Dices import Dice


class EpicKatana(Weapon):
    def __init__(self):
        super().__init__(
            name="Epic Katana",
            description="Eine geschmiedete Klinge mit Blutrinne",
            price=400,
            rarity=Rarity.EPIC,
            kampftechnik=Kampftechnik.Zweihandschwerter,
            tp=Dice(10) + 3,
            pa_bonus=2,
            at_bonus=3
        )
