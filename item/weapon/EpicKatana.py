from game import Player
from item import Rarity
from item import Weapon
from npc import Enemy


class EpicKatana(Weapon):
    def __init__(self):
        super().__init__("Yorukaze (night wind), Katana", 25, Rarity.EPIC, 16, 0.3, 3, 50)

    def attack(self, player: Player, attacks: Enemy) -> int:
        self.default_wear()
        return self.default_attack()
