from item.Item import Item
from item.usable.Usable import Usable, EffectType
from item.Rarity import Rarity

class Curry(Item, Usable):
    def __init__(self, name="Curry", description="Aromatic curry", price=9, rarity=Rarity.COMMON, heal_amount=5):
        super().__init__(name, description, price, rarity)
        self.heal_amount = heal_amount

    def consume(self, player) -> list[(int | str, EffectType)]:
        return [
            (self.heal_amount, EffectType.HEAL),
            ("It tastes amazing...", EffectType.TEXT)
        ]