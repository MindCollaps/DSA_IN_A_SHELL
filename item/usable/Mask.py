from item.Item import Item
from item.usable.Usable import Usable, EffectType
from item.Rarity import Rarity

class Mask(Item, Usable):
    def __init__(self):
        super().__init__("Kanekis Mask", "The Mask is black, it covers the right eye and lower half of the face", 20,
                        Rarity.RARE)
        self.strength_amount = 15

    def consume(self, player) -> list[(int | str, EffectType)]:
        return [(self.strength_amount, EffectType.STRENGTH),
                ("You're feeling the strength of a berserker, ready to eat some flesh. You start cracking your knuckles",
                    EffectType.TEXT)]
