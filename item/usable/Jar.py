from item.Item import Item
from item.usable.Usable import Usable, EffectType
from item.Rarity import Rarity


class Jar(Item, Usable):
    def __init__(self):
        super().__init__("Jar", "Its a mystic jar full of dirt", 5, Rarity.RARE)
        self.heal_amount = 10

    def consume(self, player) -> list[(int | str, EffectType)]:
        return [(self.heal_amount, EffectType.HEAL),
                ("I got a jar of dirt, I got a jar of dirt, and guess what's inside it", EffectType.TEXT)]
