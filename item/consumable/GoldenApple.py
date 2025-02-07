from item import Item, EffectType, Consumable, Rarity


class GoldenApple(Item, Consumable):
    def __init__(self):
        super().__init__("Golden Apple", "Its a beautiful, shiny golden apple", 30, Rarity.RARE)
        self.heal_amount = 10
        self.strength_amount = 10

    def consume(self, player) -> [(int|str, EffectType)]:
        return [(self.heal_amount, EffectType.HEAL),(self.strength_amount, EffectType.STRENGTH),
                ("You're feeling like a fresh born, full of strength and ready to fight.", EffectType.TEXT)]