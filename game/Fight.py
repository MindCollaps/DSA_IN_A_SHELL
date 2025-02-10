from game import Player
from npc import Enemy
from utils import Printer
from utils.ConsolePrinter import options_from_str_list
from utils.dice.Dices import Dice


class Fight:
    def __init__(self, printer: Printer, player: Player, enemy: Enemy):
        self.round: int = 0
        self.turn: bool = True  # True = player, False = enemy
        self.player: Player = player
        self.enemy: Enemy = enemy
        self.printer = printer
        self.runned = False

    def start(self):
        while self.player.base_hp > 0 and self.enemy.base_hp > 0 and not self.runned:
            self.new_round()

    def new_round(self):
        self.printer.clear()
        if self.turn:
            self.round += 1
            self.fight_dialogue()
        else:
            dmg = self.enemy.attack(self.player)
            self.printer.println(f"{self.enemy.name}'s Turn\n")
            self.printer.println(f"{self.enemy.name} attacks you!")
            self.printer.println(f"{self.enemy.name} makes {dmg} damage")
            self.printer.wait()
            self.player.base_hp -= dmg

        self.turn = not self.turn

    def get_enemy_status(self, hp, max_hp):
        if hp > max_hp / 2:
            return "healthy"
        elif hp > max_hp / 4:
            return "wounded"
        else:
            return "near death"

    def fight_dialogue(self):
        enemy_looking = self.get_enemy_status(self.enemy.current_hp, self.enemy.base_hp)

        self.printer.println(f"Round {self.round}\n")
        self.printer.println(f"{self.player.name} has {self.player.current_hp} HP left")
        self.printer.println(f"{self.enemy.name} is looking {enemy_looking} \n")
        self.printer.println(f"You have your {self.player.weapon_equipped.name} equipt\n")

        self.fight_menu()

    def run(self):
        self.printer.println(f"{self.player.name} tries to run away.")
        if self.player.base_hp < self.enemy.base_hp:
            self.printer.println(f"{self.player.name} is too weak to run away.")
            self.fight_menu()
        else:
            self.printer.println(f"{self.player.name} successfully runs away.")
            self.runned = True

    def fight_menu(self):
        options = ["Attack", "Use Item", "Run"]
        choice, _ = self.printer.menu(options_from_str_list(options))
        if choice == 0:
            self.attack_player()
        elif choice == 1:
            self.player.inventory.inventory_dialog_fight()
        elif choice == 2:
            self.run()

    def attack_enemy(self):
        self.printer.clear()

        attack_roll = Dice(20).roll()
        at = self.enemy.weapon.attack_value(self.enemy, self.player)

        if attack_roll <= at:
            self.printer.println("The enemy hits you!\n")
            self.parade_dialogue() # TODO: continue here
            self.printer.println(f"Your enemy is trying {'to parade' if parade else 'to dodge'} your attack")
            parade_roll = Dice(20).roll()
            if parade and parade_roll <= pa or not parade and parade_roll <= self.enemy.aw:
                self.printer.println(f"Your enemy {'paraded' if parade else 'dodged'} your attack!")
            else:
                self.printer.println(f"Your enemy cannot {'parade' if parade else 'dodge'} your attack!\n")
                self.printer.println(f"Your weapons damage is {self.player.weapon_equipped.tp.dice_text()}")
                self.printer.println("Press Enter to Roll")
                self.printer.wait()
                roll, dmg = self.player.weapon_equipped.damage_roll()
                self.printer.println(roll)
                self.printer.println(f"You deal {dmg} to {self.enemy.name}!")
                self.enemy.current_hp -= dmg
        else:
            self.printer.println("You miss your enemy!")
            self.printer.println("Press enter to continue")
            self.printer.wait()

    def attack_player(self):
        self.printer.println("Press Enter to Roll")
        self.printer.wait()
        self.printer.clear()

        attack_roll = Dice(20).roll()
        self.printer.println(f"You rolled {attack_roll}")
        at = self.player.weapon_equipped.attack_value(self.player, self.enemy)

        if attack_roll <= at:
            self.printer.println("You hit your target!\n")
            pa = self.enemy.weapon.parade_value(self.enemy, self.player)
            parade = pa >= self.enemy.aw
            self.printer.println(f"Your enemy is trying {'to parade' if parade else 'to dodge'} your attack")
            parade_roll = Dice(20).roll()
            if parade and parade_roll <= pa or not parade and parade_roll <= self.enemy.aw:
                self.printer.println(f"Your enemy {'paraded' if parade else 'dodged'} your attack!")
            else:
                self.printer.println(f"Your enemy cannot {'parade' if parade else 'dodge'} your attack!\n")
                self.printer.println(f"Your weapons damage is {self.player.weapon_equipped.tp.dice_text()}")
                self.printer.println("Press Enter to Roll")
                self.printer.wait()
                roll, dmg = self.player.weapon_equipped.damage_roll()
                self.printer.println(roll)
                self.printer.println(f"You deal {dmg} to {self.enemy.name}!")
                self.enemy.current_hp -= dmg
        else:
            self.printer.println("You miss your enemy!")
            self.printer.println("Press enter to continue")
            self.printer.wait()

