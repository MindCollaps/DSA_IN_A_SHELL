from game import Player
from item import Item
from item import Consumable


class HealthPotion(Item, Consumable):
    def __init__(self, name, price, rarity, heal_amount):
        super().__init__(name, price, rarity)
        self.heal_amount = heal_amount

    def consume(self, player: Player) -> None:
        if player.hp + self.heal_amount > player.max_hp:
            player.hp = player.max_hp