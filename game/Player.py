from game.Character import Character, Spezies
from game.Inventory import Inventory
from game.LeitEigenschaft import LeitEigenschaft
from game.LevelingSystem import LevelSystem
from item.usable.Usable import EffectType
from item.usable.Usable import Usable
from item.weapon.Fist import Fist


class Player(Character):
    def __init__(self, name: str):
        super().__init__(name, Spezies.Mensch)
        self.level = 1
        self.xp = 0
        self.xp_to_next = LevelSystem.xp_for_level(self.level)
        self.inventory = Inventory()
        self.weapon_equipped = Fist()

    def gain_xp(self, amount: int):
        self.xp += amount
        while self.xp >= self.xp_to_next:
            self.level_up()

    def level_up(self):
        self.level += 1
        overflow_xp = self.xp - self.xp_to_next
        self.xp = overflow_xp
        self.xp_to_next = LevelSystem.xp_for_level(self.level)
        self.current_hp = self.base_hp  # HP voll auffüllen

        print(f"\n=== LEVEL {self.level} ERREICHT ===")
        print("Wähle eine Eigenschaft zu verbessern:")
        for idx, eigenschaft in enumerate(LeitEigenschaft):
            print(f"{idx + 1}. {eigenschaft.name_de}")

        while True:
            try:
                choice = int(input("Auswahl (1-8): ")) - 1
                selected = list(LeitEigenschaft)[choice]
                self.increase_attribute(selected)
                print(f"{selected.value} erhöht!")
                break
            except (ValueError, IndexError):
                print("Ungültige Eingabe!")

    def increase_attribute(self, eigenschaft: LeitEigenschaft):
        # Bestehende Leit-Eigenschaft erhöhen
        for idx, (le, wert) in enumerate(self.leit_eigenschaft):
            if le == eigenschaft:
                self.leit_eigenschaft[idx] = (le, wert + 1)
                break

    def equip_weapon(self, weapon):
        self.weapon_equipped = weapon

    def consume(self, item: Usable, printer):
        effect: list[(int | str, EffectType)] = item.consume(self)

        for i in effect:
            match i[1]:
                case EffectType.HEAL:
                    heal = i[0]
                    heal -= self.base_hp - (heal + self.current_hp)
                    self.current_hp += heal
                    break

                case EffectType.SELF_HARM:
                    harm = i[0]
                    self.current_hp -= harm
                    break

                case EffectType.TEXT:
                    text = i[0]
                    printer.println(text)

        self.inventory.remove_item(item)
