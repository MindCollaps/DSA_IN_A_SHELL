from game import Dungeon

if __name__ == "__main__":
    dungeon = Dungeon.Dungeon()
    dungeon.generate_dungeon(10)
    dungeon.print_dungeon()