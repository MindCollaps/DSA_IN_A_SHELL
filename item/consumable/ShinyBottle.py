from item import Item, Consumable, EffectType, Rarity


class ShinyBottle(Item, Consumable):
    def __init__(self):
        super().__init__("Shiny Bottle", "Its a bottle, filled with a shiny, golden liquid.", 30, Rarity.EPIC)
        self.strength_amount = 15
        self.health_amount = 15

    def consume(self, player) -> [(int|str, EffectType)]:
        return [(self.health_amount, EffectType.HEAL), (self.strength_amount, EffectType.STRENGTH),
                ("You're whole body feels shiny inside. You're stronger and healthy now.", EffectType.TEXT)]