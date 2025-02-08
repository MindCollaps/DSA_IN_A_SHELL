from item import Consumable, Item, EffectType


class HealthPotion(Item, Consumable):
    def __init__(self, name, description, price, rarity, heal_amount):
        super().__init__(name, description, price, rarity)
        self.heal_amount = heal_amount

    def consume(self, player) -> int:
        return self.heal_amount

    def getType(self) -> EffectType:
        return EffectType.HEAL
