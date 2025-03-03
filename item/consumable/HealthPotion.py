from item import Item, Consumable, EffectType


class HealthPotion(Item, Consumable):
    def __init__(self, name, description, price, rarity, heal_amount):
        super().__init__(name, description, price, rarity)
        self.heal_amount = heal_amount


    def consume(self, player) -> [(int | str, EffectType)]:
        return [(self.heal_amount, EffectType.HEAL), ("Restored vitality flows through your veins, refreshing your strength and reviving your spirit",
                EffectType.TEXT)]