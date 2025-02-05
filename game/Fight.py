from game import Player
from npc import Enemy

class Fight:
    def __init__(self, player: Player, enemy: Enemy):
        self.round: int = 0
        self.turn: bool = True # True = player, False = enemy
        self.player: Player = player
        self.enemy: Enemy = enemy

    def start(self):
        while self.player.hp > 0 and self.enemy.hp > 0:
            round()
        if self.player.hp <= 0:
            print(f"{self.player.name} has died.")
        else:
            print(f"{self.enemy.name} has died.")

    def round(self):
        self.round += 1
        print(f"Round {self.round}")
        if self.turn:
            self.enemy.hp -= self.player.attack(self.enemy)
            print(f"{self.player.name} attacked {self.enemy.name} for {self.player.attack(self.enemy)} damage.")
        else:
            self.player.hp -= self.enemy.attack(self.player)
            print(f"{self.enemy.name} attacked {self.player.name} for {self.enemy.attack(self.player)} damage.")
        self.turn = not self.turn
        print(f"{self.player.name} has {self.player.hp} hp left.")
        print(f"{self.enemy.name} has {self.enemy.hp} hp left.")
        print()