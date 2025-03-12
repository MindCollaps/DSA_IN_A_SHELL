from item.Item import Item
from item.Rarity import Rarity
from item.usable.Usable import Usable, EffectType


class Bottle(Item, Usable):
    def __init__(self, name="Bottle", description="A stinky brown liquid", price=0, rarity=Rarity.COMMON,
                 drunk_amount=10, self_harm_amount=5):
        super().__init__(name, description, price, rarity)
        self.drunk_amount = drunk_amount
        self.self_harm_amount = self_harm_amount

    def consume(self, player) -> list[(int | str, EffectType)]:
        return [
            (self.drunk_amount, EffectType.DRUNK),
            ("WHY did you drink this?!", EffectType.TEXT),
            (self.self_harm_amount, EffectType.SELF_HARM)
        ]
