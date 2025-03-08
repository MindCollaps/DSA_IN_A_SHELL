from game.Character import Character
from game.Character import Spezies


class NPC(Character):
    def __init__(self, name: str, species: Spezies):
        super().__init__(name, species)
