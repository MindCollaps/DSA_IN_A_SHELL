from item.Item import Item
from item.usable.Usable import Usable, EffectType
from item.Rarity import Rarity

class HotCurry(Item, Usable):
    def __init__(self, name="Hot Curry", description="Spicy curry", price=9, rarity=Rarity.COMMON, strength_amount=6, self_harm_amount=2):
        super().__init__(name, description, price, rarity)
        self.strength_amount = strength_amount
        self.self_harm_amount = self_harm_amount

    def consume(self, player) -> list[(int | str, EffectType)]:
        return [
            (self.strength_amount, EffectType.STRENGTH),
            ("Tears stream from your eyes...", EffectType.TEXT),
            (self.self_harm_amount, EffectType.SELF_HARM)
        ]