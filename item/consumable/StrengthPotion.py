from item import Consumable, Item, EffectType


class StrengthPotion(Item, Consumable):
    def __init__(self, name, description, price, rarity, strength_amount):
        super().__init__(name, description, price, rarity)
        self.strength_amount = strength_amount

    def consume(self, player) -> list[(int | str, EffectType)]:
        return [(self.strength_amount, EffectType.STRENGTH), ("Empowering essence courses through your muscles, amplifying your strength and unleashing your full potential.",
                EffectType.TEXT)]
