from typing import List, Dict, Tuple, Optional
from rich import print
from game import Room
import random

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
    def __init__(self):
        self.rooms: List[List[Optional[Room]]] = [[]]
        self.starting_room: tuple[int, int] = (0, 0)
        self.current_room: tuple[int, int] = (0, 0)
        self.max_width: int = 0
        self.max_height: int = 0
        self.random: random.Random = random.Random()

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

    def generate_dungeon(self, num_rooms: int) -> None:
        self.add_room_at(0, 0, Room())
        self.max_width = int(num_rooms / 1.5)
        self.max_height = int(num_rooms / 1.5)

        for i in range(num_rooms):
            room = Room()
            x, y = 0, 0
            x, y = self.select_random_room()

            possible_positions = self.get_possible_room_placement_positions(x, y)
            self.random.shuffle(possible_positions)
            for dx, dy in possible_positions:
                new_x, new_y = x + dx, y + dy
                self.add_room_at(new_x, new_y, room)

        self.current_room = self.starting_room
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
        rooms = []
        for y in range(self.max_height, -1, -1):
            for x in range(self.max_width, -1, -1):
                room = self.get_room_at(x, y)
                if room is not None:
                    if len(self.get_possible_room_placement_positions(x, y)) > 0:
                        rooms.append((x, y))

        return self.random.choice(rooms)

    def get_possible_room_placement_positions(self, x: int, y: int) -> List[Tuple[int, int]]:
        possible_positions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        if self.get_room_at(x + 1, y) is not None or self.max_width <= x:
            possible_positions.remove((1, 0))

        if self.get_room_at(x - 1, y) is not None or self.max_width <= x * -1:
            possible_positions.remove((-1, 0))

        if self.get_room_at(x, y + 1) is not None or self.max_height <= y:
            possible_positions.remove((0, 1))

        if self.get_room_at(x, y - 1) is not None or y == 0:
            possible_positions.remove((0, -1))

        return possible_positions

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

    def print_dungeon(self) -> None:
        for y in range(self.max_height, -1, -1):
            for x in range(self.max_width, -1, - 1):
                room = self.get_room_at(x, y)
                if room is None:
                    print(empty, end="")
                else:
                    neighbors = self.get_neighboring_rooms(x, y)
                    if (0, 1) in neighbors:
                        print(room_visuals_top[1], end="")
                    else:
                        print(room_visuals_top[0], end="")
            print()
            for i in range(2):
                for x in range(self.max_width, -1, - 1):
                    room = self.get_room_at(x, y)
                    if room is None:
                        print(empty, end="")
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
                        print(to_print, end="")
                print()
            for x in range(self.max_width, -1, - 1):
                room = self.get_room_at(x, y)
                if room is None:
                    print(empty, end="")
                else:
                    neighbors = self.get_neighboring_rooms(x, y)
                    if (0, -1) in neighbors:
                        print(room_visuals_bottom[1], end="")
                    else:
                        print(room_visuals_bottom[0], end="")
            print()


dungeon = Dungeon()
dungeon.generate_dungeon(10)
dungeon.print_dungeon()
