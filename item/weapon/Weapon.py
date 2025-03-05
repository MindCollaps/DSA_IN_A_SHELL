from game.Kampftechnik import Kampftechnik, get_kampftechnik_wert
from game.LeitEigenschaft import LeitEigenschaft
from game.LeitEigenschaft import get_leiteigenschaft
from item import Item
from utils.dice.Dices import Dices


class Weapon(Item):
    def __init__(self, name, description, price, rarity, kampftechnik: Kampftechnik, tp: Dices, at_bonus: int = 0,
                 pa_bonus: int = 0):
        super().__init__(name, description, price, rarity)
        self.kampftechnik: Kampftechnik = kampftechnik
        self.tp = tp
        self.at_bonus = at_bonus
        self.pa_bonus = pa_bonus

    def attack_value(self, player, attacks) -> int:
        mut = get_leiteigenschaft(player, LeitEigenschaft.MU)
        mut_modifier = max(0, (mut - 8) // 3)
        at = get_kampftechnik_wert(player, self.kampftechnik) + mut_modifier
        return at + self.at_bonus

    def parade_value(self, player, attacks) -> int:
        kampftechnik_wert = get_kampftechnik_wert(player, self.kampftechnik)
        base_pa = kampftechnik_wert // 2
        leiteigenschaft = self.kampftechnik.leiteigenschaft
        pa_modifier = max(0, (get_leiteigenschaft(player, leiteigenschaft) - 8) // 3)
        pa = base_pa + pa_modifier
        return pa + self.pa_bonus

    def damage_roll(self) -> (str, int):
        return self.tp.roll()

    def equip(self, player):
        player.weapon_equipped = self
