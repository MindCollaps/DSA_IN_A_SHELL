from game import Player
from item import Item
from item import Consumable

class Fruit(Item, Consumable):
    def __init__(self):
        super().__init__("Fruit", "A weird looking fruit.", 1)

    def use(self, player: Player):
        player.heal(10)
        print("You ate the weird fruit and restored 10 health")