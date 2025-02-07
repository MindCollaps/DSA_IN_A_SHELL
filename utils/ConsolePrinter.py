import curses
from typing import Union, List


class MenuOption:
    def __init__(self, text: str, color: int = curses.COLOR_WHITE, background: int = curses.COLOR_BLACK):
        self.text = text
        self.color = color
        self.background = background
        self.color_pair_num = -1

        curses.start_color()

class Console:
    def __init__(self):
        self.screen = curses.initscr()
        self.line = 0
        self.last_x = 0

    def clear(self):
        self.line = 0
        self.last_x = 0
        self.screen.clear()

    def println(self, txt: str | None=None):
        if txt is None:
            self.line += 1
            return

        self.screen.addstr(self.line, 0, txt)
        newline_count = txt.count('\n')
        self.line += 1 + newline_count

    def wait(self):
        self.screen.getch()

    def print_menu(self, menu_options: [MenuOption], selected_index: int):
        for index, option in enumerate(menu_options):
            if index == selected_index:
                self.screen.addstr(index + 1 + self.line, 0, "-> " + option.text, curses.A_REVERSE | curses.color_pair(option.color_pair_num))
            else:
                self.screen.addstr(index + 1 + self.line, 0, "   " + option.text, curses.A_NORMAL | curses.color_pair(option.color_pair_num))

    def make_colors(self, unique_colors: List, all_options: List):
        for i, color in enumerate(unique_colors):
            curses.init_pair(i+1, color.color, color.background)
            color.color_pair_num = i+1

        for color in all_options:
            if color.color_pair_num == -1:
                for unique in unique_colors:
                    if unique.color == color.color and unique.background == color.background:
                        color.color_pair_num = unique.color_pair_num
                        break

    def menu(self, menu_options: List[Union[MenuOption, str]]) -> int | None:
        self.cool_menu(menu_options)

    def cool_menu(self, menu_options: List[Union[MenuOption, str]]):
        curses.noecho()
        curses.cbreak()
        self.screen.keypad(True)
        curses.curs_set(0)

        unique_colors = []
        for i, option in enumerate(menu_options):
            if isinstance(option, str):
                menu_options[i] = MenuOption(option)

            found = False
            for unique_color in unique_colors:
                if unique_color.color == menu_options[i].color and unique_color.background == menu_options[i].background:
                    found = True
                    break

            if not found:
                unique_colors.append(menu_options[i])

        self.make_colors(unique_colors, menu_options)

        selected_index = 0
        try:
            while True:
                self.print_menu(menu_options, selected_index)
                self.screen.refresh()

                key = self.screen.getch()

                if key == curses.KEY_UP and selected_index > 0:
                    selected_index -= 1
                elif key == curses.KEY_DOWN and selected_index < len(menu_options) - 1:
                    selected_index += 1
                elif key in [curses.KEY_ENTER, ord('\n')]:
                    break
        finally:
            curses.nocbreak()
            self.screen.keypad(False)
            curses.echo()
            curses.endwin()
            curses.curs_set(1)
            return selected_index