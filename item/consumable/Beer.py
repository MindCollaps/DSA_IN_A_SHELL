
from item import Item, Consumable, EffectType, Rarity


class Beer(Item, Consumable):
    def __init__(self):
        super().__init__("Beer", "A huge glass with beer", 11, Rarity.COMMON)
        self.drunk_amount = 7

    def consume(self, player) -> [(int|str, EffectType)]:
        return [(self.drunk_amount, EffectType.DRUNK), ("Wha-, you really drank that? Are you an alcoholic?", EffectType.TEXT)]