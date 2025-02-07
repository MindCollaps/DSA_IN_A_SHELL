from game import Player
import item
from npc import Enemy
from npc.monster import Bat

class Fight:
    def __init__(self, player: Player, enemy: Enemy):
        self.round: int = 0
        self.turn: bool = True # True = player, False = enemy
        self.player: Player = player
        self.enemy: Enemy = enemy

    def start(self):
        while self.player.hp > 0 and self.enemy.hp > 0:
            self.new_round()

        if self.player.hp <= 0:
            print(f"{self.player.name} has died.")
        else:
            print(f"{self.enemy.name} has died.")

    def new_round(self):
        self.round += 1
        print(f"Round {self.round}")
        if self.turn:
            self.fight_dialogue()
        else:
            dmg = self.enemy.attack(self.player)

        self.turn = not self.turn
        print(f"{self.player.name} has {self.player.hp} hp left.")
        print(f"{self.enemy.name} has {self.enemy.hp} hp left.")
        print()

    def fight_dialogue(self):
        print(f"Round {self.round}")
        print(f"{self.player.name} is fighting {self.enemy.name}.")
        print(f"{self.player.name} has {self.player.hp} hp left.")

        enemy_looking = ""
        if self.enemy.max_hp / 2 < self.enemy.hp:
            enemy_looking = "healthy"
        elif self.enemy.max_hp / 4 < self.enemy.hp:
            enemy_looking = "wounded"
        else:
            enemy_looking = "near death"

        print(f"{self.enemy.name} is looking {enemy_looking}.")

    def run(self):
        print(f"{self.player.name} tries to run away.")
        if self.player.hp < self.enemy.hp:
            print(f"{self.player.name} is too weak to run away.")
            self.fight_menu()
        else:
            print(f"{self.player.name} successfully runs away.")

    def fight_menu(self):
        options = ["Attack", "Use Item", "Run"]
        terminal_menu = TerminalMenu(options, title="Select an option:")
        menu_entry_index = terminal_menu.show()

        if menu_entry_index == 0:
            dmg = self.player.weapon.attack(self.player, self.enemy)
            print(f"{self.player.name} attacks {self.enemy.name} for {dmg} damage.")
            self.enemy.hp -= dmg
        elif menu_entry_index == 1:
            self.player.inventory.inventory_dialog_fight()
        elif menu_entry_index == 2:
            self.run()

fight = Fight(Player(), Bat())
fight.fight_menu()