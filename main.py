from game.Dungeon import Dungeon
from game.Player import Player
from item.usable.Beer import Beer
from item.weapon.BasicSword import BasicSword

if __name__ == "__main__":
    print("Tell me your name Adventurer!")
    PlayerName = input("Name: ")
    player = Player(PlayerName)
    dungeon = Dungeon(player)
    main_weapon = BasicSword()
    player.inventory.add_item(main_weapon)
    player.equip_weapon(main_weapon)
    player.inventory.add_item(Beer())
    dungeon.start()
