from item.weapon.Fist import Fist
from npc.NPC import NPC


class Enemy(NPC):
    def __init__(self, name):
        super().__init__(name)
        self.weapon = Fist()