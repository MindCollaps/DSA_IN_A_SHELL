from game import Player
from npc import Enemy

class Fight:
    def __init__(self, player: Player, enemy: Enemy):
        self.round: int = 0
        self.turn: bool = True # True = player, False = enemy
        self.player: Player = player
        self.enemy: Enemy = enemy