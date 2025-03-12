from game.Kampftechnik import Kampftechnik
from item.Rarity import Rarity
from utils.dice.Dices import Dices


class Weapon:
    def __init__(
            self,
            name: str,
            description: str,
            price: int,
            rarity: Rarity,
            kampftechnik: Kampftechnik,
            tp: Dices,  # 🎯 Muss ein Dices-Objekt sein
            at_bonus: int = 0,  # Angriffsbonus
            pa_bonus: int = 0  # Paradebonus (optional)
    ):
        self.name = name
        self.description = description
        self.price = price
        self.rarity = rarity
        self.kampftechnik = kampftechnik
        self.tp = tp
        self.at_bonus = at_bonus
        self.pa_bonus = pa_bonus

    def attack_value(self, character) -> int:
        return self.at_bonus + character.kampftechnik_wert(self.kampftechnik)

    def parade_value(self, character) -> int:
        return self.pa_bonus + character.kampftechnik_wert(self.kampftechnik)

    def damage_roll(self) -> tuple[str, int]:
        return self.tp.roll()

    def get_description(self, character):
        return f"Weapon: {self.name} ({self.description})\nAT: {self.attack_value(character)}\nPA: {self.parade_value(character)}\nTP: {self.tp.dice_text()}"
