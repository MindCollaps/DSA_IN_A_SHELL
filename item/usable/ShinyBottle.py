from item.Item import Item
from item.usable.Usable import Usable, EffectType
from item.Rarity import Rarity

class ShinyBottle(Item, Usable):
    def __init__(self, name="Shiny Bottle", description="A bottle filled with golden liquid", price=30, rarity=Rarity.EPIC, strength_amount=15, health_amount=15):
        super().__init__(name, description, price, rarity)
        self.strength_amount = strength_amount
        self.health_amount = health_amount

    def consume(self, player) -> list[(int | str, EffectType)]:
        return [
            (self.health_amount, EffectType.HEAL),
            (self.strength_amount, EffectType.STRENGTH),
            ("Your whole body feels shiny inside...", EffectType.TEXT)
        ]