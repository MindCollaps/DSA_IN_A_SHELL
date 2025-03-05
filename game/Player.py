from game.Character import Character
from game.Geldbeutel import Geldbeutel
from game.Inventory import Inventory
from item.weapon.Fist import Fist
from item.consumable.Consumable import EffectType


class Player(Character):
    def __init__(self, name: str):
        super().__init__(name)
        self.inventory = Inventory()
        self.weapon_equipped = Fist()
        self.geldbeutel: Geldbeutel = Geldbeutel()

    def equip_weapon(self, weapon):
        self.weapon_equipped = weapon

    def consume(self, effect: list[(int | str, EffectType)], printer):
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

