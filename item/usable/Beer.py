from item.Item import Item
from item.usable.Usable import Usable, EffectType
from item.Rarity import Rarity

class Beer(Item, Usable):
    def __init__(self, name="Beer", description="A huge glass of beer", price=11, rarity=Rarity.COMMON, drunk_amount=7):
        super().__init__(name, description, price, rarity)
        self.drunk_amount = drunk_amount

    def consume(self, player) -> list[(int | str, EffectType)]:
        return [
            (self.drunk_amount, EffectType.DRUNK),
            ("Are you an alcoholic?", EffectType.TEXT)
        ]