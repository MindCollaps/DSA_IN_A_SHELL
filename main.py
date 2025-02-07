from game import Fight, Player
from item import BasicSword
from npc.monster import Bat
from utils import Console

if __name__ == "__main__":
    console = Console()
    player = Player(BasicSword())
    fight = Fight(console, player, Bat())
    fight.start()