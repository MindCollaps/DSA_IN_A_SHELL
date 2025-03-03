from item import Item, Consumable, EffectType, Rarity


class Mask(Item, Consumable):
    def __init__(self):
        super().__init__("Kanekis Mask", "The Mask is black, it covers the right eye and lower half of the face", 20,
                        Rarity.RARE)
        self.strength_amount = 15

    def consume(self, player) -> [(int | str, EffectType)]:
        return [(self.strength_amount, EffectType.STRENGTH),
                ("You're feeling the strength of a berserker, ready to eat some flesh. You start cracking your knuckles",
                    EffectType.TEXT)]
