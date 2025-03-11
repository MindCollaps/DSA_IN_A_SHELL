import random
from typing import List, Tuple, Optional
from xml.etree.ElementTree import tostring

from utils.ConsolePrinter import Printer, MenuOption
from utils.ConsolePrinter import options_from_str_list
from game.Fight import Fight
from game import Player
from npc import Enemy
from game.Room import Room, RoomType
from game.Random import ItemPossibility, MonsterPossibility
from item.Item import Item

room_visuals_top = {
    0: "╔═════╗",
    1: "╔═╝ ╚═╗",
}

room_visuals_middle = {
    0: ["║     ║", "║     ║"],
    1: ["╝     ║", "╗     ║"],
    2: ["║     ╚", "║     ╔"],
    3: ["╝     ╚", "╗     ╔"],
}

room_visuals_bottom = {
    0: "╚═════╝",
    1: "╚═╗ ╔═╝",
}

empty = "       "


class Dungeon:
    def __init__(self, player: Player):
        self.player = player
        self.printer = Printer()
        self.printer.use_layout()
        self.rooms: List[List[Optional[Room]]] = [[]]
        self.starting_room: tuple[int, int] = (0, 0)
        self.current_room: tuple[int, int] = (0, 0)
        self.max_width: int = 0
        self.max_height: int = 0
        self.random: random.Random = random.Random()
        self.show_room_description: bool = True

    def start(self):
        self.printer.println("Choose how long your Adventure should last!")
        self.dungeon_choice()
        self.printer.clear()
        self.printer.println("Alright, your Adventure starts now!")
        self.printer.wait(wait_message=True, wait_txt="Press enter to start the adventure...")
        while self.player.current_hp > 0:
            self.dungeon_dialogue()

    def dungeon_dialogue(self):
        self.printer.clear()
        status_line = f"Level: {self.player.level} | XP: {self.player.xp}/{self.player.xp_to_next}"
        self.printer.println(status_line + "\n" + self.print_dungeon())
        self.dungeon_menu()
        self.printer.clear()
        self.printer.println(self.print_dungeon())
        self.printer.wait(wait_message=True, wait_txt="Press enter to enter the room...")
        self.dungeon_room_message()
        self.printer.wait(wait_message=True, wait_txt="Press enter to continue...")

    def dungeon_room_message(self):
        currentRoom = self.get_room_at(*self.current_room)
        if currentRoom is None:
            self.printer.println("You entered a Room that does not exist!")
        elif currentRoom.Room_Type == RoomType.MONSTER:
            self.printer.println(currentRoom.description)
            if currentRoom.monster:
                self.printer.wait(wait_message=True, wait_txt="Press enter to face the monster...")  
                self.handle_monster_room()
        elif currentRoom.Room_Type == RoomType.ITEM:
            if self.show_room_description:
                self.printer.println(currentRoom.description)  
                self.handle_item_room()
        elif currentRoom.Room_Type == RoomType.EMPTY:
            if self.show_room_description:
                self.printer.println(currentRoom.description)
        elif currentRoom.Room_Type == RoomType.SHOP:
            self.handle_shop_room()

    def dungeon_menu(self):
        x, y = self.current_room
        options = []
        if self.get_room_at(x, y + 1) is not None:  # Nord
            options.append("North")
        if self.get_room_at(x, y - 1) is not None:  # Süd
            options.append("South")
        if self.get_room_at(x - 1, y) is not None:  # Osten
            options.append("East")  
        if self.get_room_at(x + 1, y) is not None:  # Westen
            options.append("West")

        options.append("Inventory") 

        if not options:
            self.printer.println("No available directions to move!")
            return

        choice, _ = self.printer.menu(options_from_str_list(options))
        if options[choice] == "North":
            self.move((0, 1))
            self.printer.println("You head toward north.")
        elif options[choice] == "East":
            self.move((-1, 0))  
            self.printer.println("You head toward east.")
        elif options[choice] == "West":
            self.move((1, 0)) 
            self.printer.println("You head toward west.")
        elif options[choice] == "South":
            self.move((0, -1))
            self.printer.println("You head toward south.")
        elif options[choice] == "Inventory":
            self.open_inventory()


    def open_inventory(self):
        action, close = self.player.inventory.inventory_dialog(self.printer, self.player, fight=False)
        
        if close:
            self.printer.clear()
            self.dungeon_dialogue()
        elif action:
            self.printer.clear()
            self.dungeon_dialogue()


    def handle_monster_room(self):
        currentRoom = self.get_room_at(*self.current_room)
        if currentRoom and currentRoom.monster:
            fight = Fight(self.player, currentRoom.monster)
            outcome = fight.start()


            if outcome == "win":
                currentRoom.Room_Type = RoomType.EMPTY
                currentRoom.description = "Der Gegner wurde besiegt. Der Raum ist jetzt leer."
                currentRoom.monster = None  # Entferne das Monster aus dem Raum
            elif outcome == "fled":
                pass
            elif outcome == "lose":
                currentRoom.description = "Du wurdest besiegt. Der Gegner bewacht diesen Raum."

    def handle_shop_room(self):
        from game.Shop import Shop
        Shop(self.player).start_shop()
        current_room = self.get_room_at(*self.current_room)
        current_room.Room_Type = RoomType.EMPTY  # Shop nach Besuch schließen


    def handle_item_room(self):
        room = self.get_room_at(*self.current_room)
        if room and room.items:
            for item in room.items:
                self.player.inventory.add_item(item)
                self.printer.println(f"{item.name} wurde deinem Inventar hinzugefügt!")
            self.printer.wait(wait_message=True)
            room.Room_Type = RoomType.EMPTY #Item nach aufsammeln entfernen

    def move(self, direction: tuple[int, int]) -> bool:
        x, y = self.current_room
        new_x, new_y = x + direction[0], y + direction[1]
        if self.get_room_at(new_x, new_y) is not None:
            self.current_room = (new_x, new_y)
            return True
        else:
            return False

    def set_noise_seed(self, seed: int) -> None:
        g = random.Random()
        g.seed(seed)
        self.random.setstate(g.getstate())

    def dungeon_choice(self,):
        options = ["Small", "Middle", "Big",]
        choice, _ = self.printer.menu(options_from_str_list(options))
        if choice == 0 :
            self.generate_dungeon(20)
        elif choice == 1 :
            self.generate_dungeon(30)
        elif choice == 2 :
            self.generate_dungeon(40)

    def generate_dungeon(self, num_rooms: int) -> None:
        self.rooms = [[Room(self)]]
        self.starting_room = (0, 0)
        self.current_room = (0, 0)
        self.max_width = 0
        self.max_height = 0

        rooms_added = 1
        failsafe = 0

        while rooms_added < num_rooms and failsafe < 1000:
            x, y = self.select_random_room()
            possible = self.get_possible_room_placement_positions(x, y)

            if not possible:
                failsafe += 1
                continue

            dx, dy = random.choice(possible)
            new_x, new_y = x + dx, y + dy

            if not self.get_room_at(new_x, new_y):
                new_room = Room(self)
                if random.randint(1, 10) == 1:
                    new_room.Room_Type = RoomType.SHOP
                    new_room.description = "Ein mysteriöser Shop"

                self.add_room_at(new_x, new_y, new_room)
                rooms_added += 1
                self.max_width = max(self.max_width, new_x)
                self.max_height = max(self.max_height, new_y)
                failsafe = 0

        self.shrink_dungeon()

    def select_random_dead_end(self) -> Tuple[int, int]:
        dead_ends = []
        max_y = self.max_height

        while len(dead_ends) == 0:
            # Check rows and columns from max_width and height to max_x and max_y
            for y in range(self.max_height, max_y - 1, -1):
                for x in range(self.max_width, -1, -1):
                    room = self.get_room_at(x, y)
                    if room is not None:
                        dead_ends.append((x, y))

            for y in range(self.max_height, -1, -1):
                for x in range(self.max_width, max_y - 1, -1):
                    room = self.get_room_at(x, y)
                    if room is not None:
                        dead_ends.append((x, y))

            max_y -= 1

        return self.random.choice(dead_ends)

    def select_random_room(self) -> Tuple[int, int]:
        valid_rooms = []
        for y in range(len(self.rooms)):
            for x in range(len(self.rooms[y])):
                if self.rooms[y][x] and self.get_possible_room_placement_positions(x, y):
                    valid_rooms.append((x, y))

        if not valid_rooms:
            return (0, 0)  # Fallback zum Startraum

        return random.choice(valid_rooms)

    def get_possible_room_placement_positions(self, x: int, y: int) -> List[Tuple[int, int]]:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        possible = []

        for dx, dy in directions:
            new_x = x + dx
            new_y = y + dy
            if new_x < 0 or new_y < 0:
                continue
            if not self.get_room_at(new_x, new_y):
                possible.append((dx, dy))

        return possible

    def get_neighboring_rooms(self, x: int, y: int) -> List[Tuple[int, int]]:
        possible_positions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        if self.get_room_at(x + 1, y) is None:
            possible_positions.remove((1, 0))

        if self.get_room_at(x - 1, y) is None:
            possible_positions.remove((-1, 0))

        if self.get_room_at(x, y + 1) is None:
            possible_positions.remove((0, 1))

        if self.get_room_at(x, y - 1) is None:
            possible_positions.remove((0, -1))

        return possible_positions

    def add_room_at(self, x: int, y: int, room: Optional[Room]):
        if x == -1:
            self.rooms = self.shift_left(self.rooms)
            x = 0

        while len(self.rooms) <= y:
            self.rooms.append([])
        while len(self.rooms[y]) <= x:
            self.rooms[y].append(None)
        self.rooms[y][x] = room

    def shift_left(self, arr: List[List[Optional[Room]]]) -> List[List[Optional[Room]]]:
        for row in arr:
            row.insert(0, None)

        self.starting_room = (self.starting_room[0] + 1, self.starting_room[1])
        return arr

    def get_room_at(self, x: int, y: int) -> Optional[Room]:
        if 0 <= y < len(self.rooms) and 0 <= x < len(self.rooms[y]):
            return self.rooms[y][x]
        return None

    def shrink_dungeon(self) -> None:
        max_y = 0
        max_x = 0
        for y in range(self.max_height, -1, -1):
            for x in range(self.max_width, -1, -1):
                room = self.get_room_at(x, y)
                if room is not None:
                    if y > max_y:
                        max_y = y
                    if x > max_x:
                        max_x = x

        self.max_height = max_y
        self.max_width = max_x

    def has_wall(self, x, y) -> list[(int, int)]:
        room = self.get_room_at(x, y)
        if room is None:
            return []

        return room.walls

    def print_dungeon(self) -> str:
        dungeonText = ""
        for y in range(self.max_height, -1, -1):
            for x in range(self.max_width, -1, - 1):
                room = self.get_room_at(x, y)
                if room is None:
                    dungeonText += empty
                else:
                    neighbors = self.get_neighboring_rooms(x, y)
                    if (0, 1) in neighbors:
                        dungeonText += room_visuals_top[1]
                    else:
                        dungeonText += room_visuals_top[0]
            dungeonText += "\n"
            for i in range(2):
                for x in range(self.max_width, -1, - 1):
                    room = self.get_room_at(x, y)
                    if room is None:
                        dungeonText += empty
                    else:
                        neighbors = self.get_neighboring_rooms(x, y)
                        to_print = ""
                        if (1, 0) in neighbors and (-1, 0) in neighbors:
                            to_print = room_visuals_middle[3][i]
                        elif (1, 0) in neighbors:
                            to_print = room_visuals_middle[1][i]
                        elif (-1, 0) in neighbors:
                            to_print = room_visuals_middle[2][i]
                        else:
                            to_print = room_visuals_middle[0][i]

                        if i == 1:
                            if self.current_room == (x, y):
                                to_print = to_print[:3] + "X" + to_print[4:]
                        dungeonText += to_print
                dungeonText += "\n"
            for x in range(self.max_width, -1, - 1):
                room = self.get_room_at(x, y)
                if room is None:
                    dungeonText += empty
                else:
                    neighbors = self.get_neighboring_rooms(x, y)
                    if (0, -1) in neighbors:
                        dungeonText += room_visuals_bottom[1]
                    else:
                        dungeonText += room_visuals_bottom[0]
            dungeonText += "\n"

        return dungeonText
