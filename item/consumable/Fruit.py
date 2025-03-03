from item import Item, Consumable, EffectType, Rarity


class Fruit(Item, Consumable):
    def __init__(self):
        super().__init__("Fruit",
            "The fruit pulsed with a slow, internal rhythm, its skin a mottled tapestry of bruised purples and sickly greens.",
            3, Rarity.COMMON)
        self.heal_amount = 5

    def consume(self, player) -> [(int | str, EffectType)]:
        return [(self.heal_amount, EffectType.HEAL),
                ("It tasted so weird also good, you're confused now", EffectType.TEXT)]
