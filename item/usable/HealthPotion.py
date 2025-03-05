from item.Item import Item
from item.usable.Usable import Usable, EffectType


class HealthPotion(Item, Usable):
    def __init__(self, name, description, price, rarity, heal_amount):
        super().__init__(name, description, price, rarity)
        self.heal_amount = heal_amount

    def consume(self, player) -> list[(int | str, EffectType)]:
        return [(self.heal_amount, EffectType.HEAL), ("Restored vitality flows through your veins, refreshing your strength and reviving your spirit",
                EffectType.TEXT)]