class Player:
    def __init__(self, weapon):
        from game import Inventory
        from item import Weapon

        self.name = "Player"
        self.level: int = 1
        self.xp: int = 0
        self.hp: int = 100
        self.max_hp: int = 100
        self.inventory: Inventory = Inventory()
        self.gold: int = 30
        self.weapon: Weapon = weapon