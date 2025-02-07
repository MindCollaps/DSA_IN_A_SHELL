from . import Player
from npc import Enemy
from utils import Console


class Fight:
    def __init__(self, console: Console, player: Player, enemy: Enemy):
        self.round: int = 0
        self.turn: bool = True  # True = player, False = enemy
        self.player: Player = player
        self.enemy: Enemy = enemy
        self.console = console
        self.runned = False

    def start(self):
        while self.player.hp > 0 and self.enemy.hp > 0:
            self.new_round()
            if self.player.hp <= 0 or self.enemy.hp <= 0:
                break

    def new_round(self):
        self.console.clear()
        if self.turn:
            self.round += 1
            self.fight_dialogue()
        else:
            dmg = self.enemy.attack(self.player)
            txt = f"""{self.enemy.name} attacks you!
                    {self.enemy.name} makes {dmg} damage"""
            self.console.println(txt)
            self.console.wait()
            self.player.hp -= dmg

        self.turn = not self.turn

    def get_enemy_status(self, hp, max_hp):
        if hp > max_hp / 2:
            return "healthy"
        elif hp > max_hp / 4:
            return "wounded"
        else:
            return "near death"

    def fight_dialogue(self):
        enemy_looking = self.get_enemy_status(self.enemy.hp, self.enemy.max_hp)

        txt = f"""Round {self.round}
        {self.player.name} has {self.player.hp} HP left
        {self.enemy.name} is looking {enemy_looking}"""

        self.console.println(txt)
        self.fight_menu()

    def run(self):
        self.console.println(f"{self.player.name} tries to run away.")
        if self.player.hp < self.enemy.hp:
            self.console.println(f"{self.player.name} is too weak to run away.")
            self.fight_menu()
        else:
            self.console.println(f"{self.player.name} successfully runs away.")
            self.runned = True

    def fight_menu(self):
        options = ["Attack", "Use Item", "Run"]
        choice = self.console.menu(options)

        if choice == 0:
            dmg = self.player.weapon.attack(self.player, self.enemy)
            print(f"{self.player.name} attacks {self.enemy.name} for {dmg} damage.")
            self.enemy.hp -= dmg
            self.console.wait()
        elif choice == 1:
            self.player.inventory.inventory_dialog_fight()
        elif choice == 2:
            self.run()
