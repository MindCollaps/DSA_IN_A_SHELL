from game.Character import Character

class Player(Character):
    def __init__(self, name: str):
        super().__init__(name)
