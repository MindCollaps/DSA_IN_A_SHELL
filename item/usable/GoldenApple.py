from item.Item import Item
from item.usable.Usable import Usable, EffectType
from item.Rarity import Rarity

class GoldenApple(Item, Usable):
    def __init__(self, name="Golden Apple", description="A shiny golden apple", price=30, rarity=Rarity.RARE, heal_amount=10, strength_amount=10):
        super().__init__(name, description, price, rarity)
        self.heal_amount = heal_amount
        self.strength_amount = strength_amount

    def consume(self, player) -> list[(int | str, EffectType)]:
        return [
            (self.heal_amount, EffectType.HEAL),
            (self.strength_amount, EffectType.STRENGTH),
            ("You feel reborn with vigor...", EffectType.TEXT)
        ]