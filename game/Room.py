class Room:
    def __init__(self):
        self.description = ""
        self.items = []
        self.monsters = []
        self.walls = []
        self.generate_room()

    def generate_room(self):
        self.monsters.append("")