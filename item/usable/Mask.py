from item.Item import Item
from item.Rarity import Rarity
from item.usable.Usable import Usable, EffectType


class Mask(Item, Usable):
    def __init__(self, name="Kanekis Mask", description="Black mask covering half the face", price=20,
                 rarity=Rarity.RARE, strength_amount=15):
        super().__init__(name, description, price, rarity)
        self.strength_amount = strength_amount

    def consume(self, player) -> list[(int | str, EffectType)]:
        return [
            (self.strength_amount, EffectType.STRENGTH),
            ("You feel the strength of a berserker...", EffectType.TEXT)
        ]
