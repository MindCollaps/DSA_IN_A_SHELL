from item.Item import Item
from item.usable.Usable import Usable, EffectType
from item.Rarity import Rarity

class Stick(Item, Usable):
    def __init__(self, name="Stick", description="A simple stick that looks like a wand", price=11, rarity=Rarity.COMMON):
        super().__init__(name, description, price, rarity)

    def consume(self, player) -> list[(int | str, EffectType)]:
        return [("You're not a wizard, Harry", EffectType.TEXT)]