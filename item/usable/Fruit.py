from item.Item import Item
from item.usable.Usable import Usable, EffectType
from item.Rarity import Rarity


class Fruit(Item, Usable):
    def __init__(self):
        super().__init__("Fruit",
            "The fruit pulsed with a slow, internal rhythm, its skin a mottled tapestry of bruised purples and sickly greens.",
            3, Rarity.COMMON)
        self.heal_amount = 5

    def consume(self, player) -> list[(int | str, EffectType)]:
        return [(self.heal_amount, EffectType.HEAL),
                ("It tasted so weird also good, you're confused now", EffectType.TEXT)]
