from item import Consumable
from item import Item


class HealthPotion(Item, Consumable):
    def __init__(self, name, price, rarity, heal_amount):
        super().__init__(name, price, rarity)
        self.heal_amount = heal_amount

    def consume(self, player) -> None:
        if player.hp + self.heal_amount > player.max_hp:
            player.hp = player.max_hp