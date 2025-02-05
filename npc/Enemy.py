from abc import abstractmethod

from game import Player
from npc import NPC

class Enemy(NPC):
    def __init__(self, name: str, hp: int, max_hp: int):
        super().__init__(name)
        self.hp: int = hp
        self.max_hp: int = max_hp

    @abstractmethod
    def attack(self, player: Player) -> int:
        pass