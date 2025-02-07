
from item import Item, Rarity, Consumable, EffectType


class HotCurry(Item, Consumable):
    def __init__(self):
        super().__init__("Hot Curry", "a good smelling and spicy curry", 9, Rarity.COMMON)
        self.strength_amount = 6
        self.self_harm_amount = 2

    def consume(self, player) -> [(int|str, EffectType)]:
        return [(self.strength_amount, EffectType.STRENGTH), ("You have tears in your eyes because of the spice...", EffectType.TEXT), (self.self_harm_amount, EffectType.SELF_HARM)]