from item import Rarity
from item import Weapon


class BasicSword(Weapon):
    def __init__(self):
        super().__init__("Basic Sword", "Well its a basic sword, what did you think?", 10, Rarity.COMMON, 10, 0.1, 2,
                         100)

    def attack(self, player, attacks) -> int:
        self.default_wear()
        return self.default_attack()
