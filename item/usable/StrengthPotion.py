from item.Item import Item
from item.usable.Usable import Usable, EffectType
from item.Rarity import Rarity

class StrengthPotion(Item, Usable):
    def __init__(self, name, description, price, rarity, strength_amount):
        super().__init__(name, description, price, rarity)
        self.strength_amount = strength_amount

    def consume(self, player) -> list[tuple[int | str, EffectType]]:
        return [(self.strength_amount, EffectType.STRENGTH),
                ("Empowering essence courses through your muscles, amplifying your strength and unleashing your full potential.", EffectType.TEXT)]
