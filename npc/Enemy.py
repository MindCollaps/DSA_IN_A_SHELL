from npc.NPC import NPC


class Enemy(NPC):
    def __init__(self, name, weapon, species):
        super().__init__(name, species)
        self.weapon = weapon
