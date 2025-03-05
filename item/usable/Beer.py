from item.Item import Item
from item.usable.Usable import Usable, EffectType
from item.Rarity import Rarity


class Beer(Item, Usable):
    def __init__(self):
        super().__init__("Beer", "A huge glass with beer", 11, Rarity.COMMON)
        self.drunk_amount = 7

    def consume(self, player) -> list[(int | str, EffectType)]:
        return [(self.drunk_amount, EffectType.DRUNK),
                ("Wha-, you really drank that? Are you an alcoholic?", EffectType.TEXT)]
