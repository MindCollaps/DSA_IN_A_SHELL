from game import Player
from npc import Enemy
from utils import Printer, MenuOption
from utils.ConsolePrinter import options_from_str_list
from utils.dice.Dices import Dice


class Fight:
    def __init__(self, player: Player, enemy: Enemy):
        self.round: int = 0
        self.turn: bool = True  # True = player, False = enemy
        self.player: Player = player
        self.enemy: Enemy = enemy
        self.printer = Printer()
        self.printer.use_layout()
        self.runned = False

    def start(self):
        while self.player.current_hp > 0 and self.enemy.current_hp > 0 and not self.runned:
            self.new_round()

        self.printer.clear()

        if self.player.current_hp <= 0:
            self.printer.println("You died!")
        elif self.enemy.current_hp <= 0:
            self.printer.println(f"You defeated {self.enemy.name}!")

        self.printer.wait(wait_message=True)
        # TODO: Add some color maybe?

    def new_round(self):
        self.printer.clear()
        if self.turn:
            self.round += 1
            self.fight_dialogue()
        else:
            self.printer.println("Its your enemies turn!")
            self.printer.wait(wait_message=True)
            self.printer.clear()
            self.attack_enemy()

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
        options = ["Attack", "Use Item", "Try to run"]
        choice, _ = self.printer.menu(options_from_str_list(options))
        if choice == 0:
            self.attack_player()
        elif choice == 1:
            self.player.inventory.inventory_dialog_fight()
        elif choice == 2:
            self.run()

    def attack_enemy(self):
        attack_roll = Dice(20).roll()
        at = self.enemy.weapon.attack_value(self.enemy, self.player)

        if attack_roll <= at:
            self.printer.println(f"\n{self.enemy.name} hits you!\n")
            self.parade_player()
        else:
            self.printer.println("\nThe enemy misses you!")
            self.printer.wait(wait_message=True)

    def parade_player(self):
        pa = self.player.weapon_equipped.parade_value(self.player, self.enemy)
        self.printer.println(f"You can dodge ({self.player.aw}) or try to parade ({pa})")
        options = [MenuOption(f"Dodge ({self.player.aw})"), MenuOption(f"Parade ({pa})")]
        choice, _ = self.printer.menu(options)
        dodge_txt = "dodge" if choice == 0 else "parade"
        self.printer.println(f"\nYou try to {dodge_txt}!")
        if choice == 0:
            self.printer.println(f"Your AW value is {self.player.aw}\n")
        elif choice == 1:
            self.printer.println(f"Your weapons PA is {pa}\n")

        self.printer.wait(wait_message=True, wait_txt="Press enter to roll")
        roll = Dice(20).roll()
        self.printer.println(f"\nYou rolled {roll}\n\n")

        if choice == 0 and roll <= self.player.aw:
            self.printer.println("You dodged the attack!")
        elif choice == 1 and roll <= pa:
            self.printer.println("You parade the attack!")
        else:
            self.printer.println(f"You fail to {dodge_txt} the attack")
            _, dmg = self.enemy.weapon.damage_roll()
            self.printer.println(f"{self.enemy.name} deals {dmg} damage to you!")
            self.player.current_hp -= dmg

        self.printer.wait(wait_message=True)

    def attack_player(self):
        self.printer.clear()
        at = self.player.weapon_equipped.attack_value(self.player, self.enemy)
        self.printer.println("You try to attack!")
        self.printer.println(f"Your {self.player.weapon_equipped.name}s AT is {at}\n")
        self.printer.wait(wait_message=True, wait_txt="Press enter to roll")

        attack_roll = Dice(20).roll()
        self.printer.println(f"You rolled {attack_roll}")

        if attack_roll <= at:
            self.printer.println("You hit your target!\n")
            self.printer.wait(wait_message=True)
            pa = self.enemy.weapon.parade_value(self.enemy, self.player)
            parade = pa >= self.enemy.aw
            self.printer.println(f"Your enemy is trying {'to parade' if parade else 'to dodge'} your attack")
            parade_roll = Dice(20).roll()
            if parade and parade_roll <= pa or not parade and parade_roll <= self.enemy.aw:
                self.printer.println(f"Your enemy {'paraded' if parade else 'dodged'} your attack!")
            else:
                self.printer.println(f"Your enemy cannot {'parade' if parade else 'dodge'} your attack!\n")
                self.printer.println(f"Your weapons damage is {self.player.weapon_equipped.tp.dice_text()}")
                self.printer.wait(wait_message=True, wait_txt="Press enter to roll")
                roll, dmg = self.player.weapon_equipped.damage_roll()
                self.printer.println(f"\n{roll}")
                self.printer.println(f"\nYou deal {dmg} damage to {self.enemy.name}!")
                self.enemy.current_hp -= dmg
        else:
            self.printer.println("You miss your enemy!")

        self.printer.wait(wait_message=True)
