from item.Item import Item
from item.usable.Usable import Usable, EffectType
from item.Rarity import Rarity


class HotCurry(Item, Usable):
    def __init__(self):
        super().__init__("Hot Curry", "a good smelling and spicy curry", 9, Rarity.COMMON)
        self.strength_amount = 6
        self.self_harm_amount = 2

    def consume(self, player) -> list[(int | str, EffectType)]:
        return [(self.strength_amount, EffectType.STRENGTH),
                ("You have tears in your eyes because of the spice...", EffectType.TEXT),
                (self.self_harm_amount, EffectType.SELF_HARM)]
