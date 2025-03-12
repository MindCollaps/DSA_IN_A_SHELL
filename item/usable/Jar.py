from item.Item import Item
from item.Rarity import Rarity
from item.usable.Usable import Usable, EffectType


class Jar(Item, Usable):
    def __init__(self, name="Jar", description="A jar full of dirt", price=5, rarity=Rarity.RARE, heal_amount=10):
        super().__init__(name, description, price, rarity)
        self.heal_amount = heal_amount

    def consume(self, player) -> list[(int | str, EffectType)]:
        return [
            (self.heal_amount, EffectType.HEAL),
            ("I got a jar of dirt...", EffectType.TEXT)
        ]
