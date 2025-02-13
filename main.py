from game import Player, Fight
from npc.monster import Bat

if __name__ == "__main__":
    player = Player("Tim")
    enemy = Bat()
    fight = Fight(player, enemy)
    fight.start()
