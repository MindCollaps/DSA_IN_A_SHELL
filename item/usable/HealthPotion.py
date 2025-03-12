from item.Item import Item
from item.Rarity import Rarity
from item.usable.Usable import Usable, EffectType


class HealthPotion(Item, Usable):
    def __init__(self, name="Health Potion", description="Restores health", price=50, rarity=Rarity.COMMON,
                 heal_amount=10):
        super().__init__(name, description, price, rarity)
        self.heal_amount = heal_amount

    def consume(self, player):
        player.heal(self.heal_amount)
        return [(f"Restored {self.heal_amount} HP!", EffectType.TEXT)]
