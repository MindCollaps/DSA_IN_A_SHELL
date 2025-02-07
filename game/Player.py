import game
import item


class Player:
    def __init__(self):
        self.name = "Player"
        self.level: int = 1
        self.xp: int = 0
        self.hp: int = 100
        self.max_hp: int = 100
        self.inventory: game.Inventory = game.Inventory()
        self.gold: int = 30
        self.weapon: item.Weapon | None = None