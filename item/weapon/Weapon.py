import random
from abc import abstractmethod

from game.Kampftechnik import Kampftechnik, get_kampftechnik_wert
from item import Item
from utils import Dices


class Weapon(Item):
    def __init__(self, name, description, price, rarity, kampftechnik: Kampftechnik, tp: Dices):
        super().__init__(name, description, price, rarity)
        self.kampftechnik: Kampftechnik = kampftechnik
        self.tp = tp

    def get_at(self, player, attacks) -> int:
        mut = player.leit_eigenschaft.mut
        mut_modifier = max(0, (mut - 8) // 3)
        at = get_kampftechnik_wert(player, self.kampftechnik) + mut_modifier
        return at

    def get_pa(self, player, attacks) -> int:
        kampftechnik_wert = get_kampftechnik_wert(player, self.kampftechnik)
        base_pa = kampftechnik_wert // 2
        leiteigenschaft = self.kampftechnik.leiteigenschaft
        pa_modifier = max(0, (player.leit_eigenschaft[leiteigenschaft.value].value - 8) // 3)
        pa = base_pa + pa_modifier
        return pa

    def damage_roll(self) -> (str, int):
        return self.tp.roll()

    def equip(self, player):
        player.weapon = self
