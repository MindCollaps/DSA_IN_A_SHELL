from item.Item import Item
from item.usable.Usable import Usable, EffectType
from item.Rarity import Rarity

class Stone(Item, Usable):
    def __init__(self, name="Stone", description="A limestone rock", price=11, rarity=Rarity.COMMON, self_harm_amount=3):
        super().__init__(name, description, price, rarity)
        self.self_harm_amount = self_harm_amount

    def consume(self, player) -> list[(int | str, EffectType)]:
        return [
            ("Why are you hitting yourself?", EffectType.TEXT),
            (self.self_harm_amount, EffectType.SELF_HARM)
        ]