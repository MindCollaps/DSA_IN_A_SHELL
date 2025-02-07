from game import Fight, Player
from npc.monster import Bat
from utils import Console

if __name__ == "__main__":
    console = Console()
    fight = Fight(console, Player(), Bat())
    fight.start()