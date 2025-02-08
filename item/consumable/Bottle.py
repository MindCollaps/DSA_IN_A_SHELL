from item import Item, Consumable, EffectType, Rarity


class Bottle(Item, Consumable):
    def __init__(self):
        super().__init__("Bottle", "A bottle filled with a stinky, brown liquid.", 0, Rarity.COMMON)
        self.drunk_amount = 10
        self.self_harm_amount = 5

    def consume(self, player) -> [(int | str, EffectType)]:
        return [(self.drunk_amount, EffectType.DRUNK), ("Excuse yourself, what the-? WHY?", EffectType.TEXT),
                self.self_harm_amount, EffectType.SELF_HARM]
