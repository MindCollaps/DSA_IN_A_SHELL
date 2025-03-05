from game.Character import Character


class NPC(Character):
    def __init__(self, name: str, species):
        super().__init__(name, species)
