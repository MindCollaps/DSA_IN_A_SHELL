from item.Item import Item
from item.usable.Usable import Usable, EffectType
from item.Rarity import Rarity


class Stick(Item, Usable):
    def __init__(self):
        super().__init__("Stick", "A simple Stick, looks like a wand", 11, Rarity.COMMON)

    def consume(self, player) -> list[(int | str, EffectType)]:
        return [("You're not a wizard, Harry", EffectType.TEXT)]
