from npc.NPC import NPC


class Enemy(NPC):
    def __init__(self, name, weapon):
        super().__init__(name)
        self.weapon = weapon
