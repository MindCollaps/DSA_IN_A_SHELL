from item import Item, Rarity, Consumable, EffectType


class Curry(Item, Consumable):
    def __init__(self):
        super().__init__("Curry", "Its a good smelling curry.", 9, Rarity.COMMON)
        self.heal_amount = 5

    def consume(self, player) -> list[(int | str, EffectType)]:
        return [(self.heal_amount, EffectType.HEAL),
                ("It tasted so good, you're feeling great again.", EffectType.TEXT)]
