from game.Player import Player
from game.Fight import Fight
from item.usable.Beer import Beer
from item.weapon.Plank import Plank
from item.weapon.SoapSock import SoapSock
from npc.monster import Bat
from utils import Printer
from game.Dungeon import Dungeon

if __name__ == "__main__":
    player = Player("Tim")
    player.inventory.add_item(Plank())
    player.inventory.add_item(Beer())
    player.inventory.add_item(SoapSock())
    game = Dungeon(player)
    game.start()

    enemy = Bat()
    fight = Fight(player, enemy)
    fight.start()
