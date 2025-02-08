from item import Item, Consumable, EffectType, Rarity


class Jar(Item, Consumable):
    def __init__(self):
        super().__init__("Jar", "Its a mystic jar full of dirt", 5, Rarity.RARE)
        self.heal_amount = 10

    def consume(self, player) -> [(int | str, EffectType)]:
        return [(self.heal_amount, EffectType.HEAL),
                ("I got a jar of dirt, I got a jar of dirt, and guess what's inside it", EffectType.TEXT)]
