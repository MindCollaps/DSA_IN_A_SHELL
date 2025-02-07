from item import Consumable, Item, EffectType, Rarity


class StrengthPotion(Item, Consumable):
    def __init__(self, name, description, price, rarity, strength_amount):
        super().__init__(name, description, price, rarity)
        self.strength_amount = strength_amount

    def consume(self, player) -> int:
        return self.strength_amount

    def getType(self) -> EffectType:
        return EffectType.STRENGTH