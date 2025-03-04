from npc.NPC import NPC


class Enemy(NPC):
    def __init__(self, name, weapon, current_hp, base_hp):
        super().__init__(name)
        self.weapon = weapon
        self.current_hp = current_hp
        self.base_hp = base_hp
