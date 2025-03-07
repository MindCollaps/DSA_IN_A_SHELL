from item.Item import Item
from item.usable.Usable import Usable, EffectType
from item.Rarity import Rarity


class Stone(Item, Usable):
    def __init__(self):
        super().__init__("Stone",
                        "Limestone is a sedimentary rock primarily composed of calcium carbonate (CaCO3) in the form of the minerals calcite and aragonite",
                        11, Rarity.COMMON)
        self.self_harm_amount = 3

    def consume(self, player) -> list[(int | str, EffectType)]:
        return [("Why are you hitting yourself?", EffectType.TEXT), (self.self_harm_amount, EffectType.SELF_HARM)]
