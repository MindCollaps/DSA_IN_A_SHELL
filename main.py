from game import Player, Fight
from item.consumable.Beer import Beer
from item.weapon.Plank import Plank
from item.weapon.SoapSock import SoapSock
from npc.monster import Bat
from utils import Printer

if __name__ == "__main__":
    player = Player("Tim")
    player.inventory.add_item(Plank())
    player.inventory.add_item(Beer())
    player.inventory.add_item(SoapSock())
    enemy = Bat()
    fight = Fight(player, enemy)
    fight.start()
