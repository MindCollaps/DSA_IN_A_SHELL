from game.Player import Player
from item.usable.Beer import Beer
from item.weapon.EpicKatana import EpicKatana
from item.weapon.Plank import Plank
from item.weapon.SoapSock import SoapSock
from game.Dungeon import Dungeon

if __name__ == "__main__":
    player = Player("Tim")
    game = Dungeon(player)
    player.inventory.add_item(Plank())
    player.inventory.add_item(Beer())
    player.inventory.add_item(SoapSock())
    player.inventory.add_item(EpicKatana())
    game.start()
