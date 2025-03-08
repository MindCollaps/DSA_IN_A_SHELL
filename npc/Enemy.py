from npc.NPC import NPC
from game.Character import Spezies


class Enemy(NPC):
    def __init__(self, name: str, weapon, species: Spezies,):
        super().__init__(name, species)
        if isinstance(weapon, list):
            self.weapon = weapon[0]
        else:
            self.weapon = weapon
        
        self.name = name
        self.species = species
