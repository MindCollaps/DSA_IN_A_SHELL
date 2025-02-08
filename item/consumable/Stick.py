from item import Item, Consumable, EffectType, Rarity


class Stick(Item, Consumable):
    def __init__(self):
        super().__init__("Stick", "A simple Stick, looks like a wand", 11, Rarity.COMMON)

    def consume(self, player) -> [(int | str, EffectType)]:
        return [("You're not a wizard, Harry", EffectType.TEXT)]
