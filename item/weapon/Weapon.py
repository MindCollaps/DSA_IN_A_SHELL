from abc import abstractmethod
from item import Item
from npc import Enemy
from game import Player

import random

class Weapon(Item):
    def __init__(self, name, price, rarity, damage, critical_chance, critical_damage, durability):
        super().__init__(name, price, rarity)
        self.damage: int = damage
        self.critical_chance: float = critical_chance
        self.critical_damage: int = critical_damage
        self.durability: float = durability

    @abstractmethod
    def attack(self, player: Player, attacks: Enemy) -> int:
        pass

    def default_attack(self) -> int:
        if random.random() < self.critical_chance:
            return self.damage * self.critical_damage

    def default_wear(self):
        rand = random.random()
        if rand < 0.3:
            self.durability -= 2
        elif rand < 0.6:
            self.durability -= 1

    def equip(self, player: Player):
        player.weapon = self