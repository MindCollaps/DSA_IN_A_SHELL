from item.Item import Item
from item.Rarity import Rarity
from item.usable.Usable import Usable, EffectType


class Fruit(Item, Usable):
    def __init__(self, name="Fruit", description="A strange pulsating fruit", price=3, rarity=Rarity.COMMON,
                 heal_amount=5):
        super().__init__(name, description, price, rarity)
        self.heal_amount = heal_amount

    def consume(self, player) -> list[(int | str, EffectType)]:
        return [
            (self.heal_amount, EffectType.HEAL),
            ("It tastes weirdly good...", EffectType.TEXT)
        ]
