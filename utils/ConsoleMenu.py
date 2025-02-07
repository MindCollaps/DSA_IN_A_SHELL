import curses

def print_menu(stdscr, menu_options, selected_index):
    for i, option in enumerate(menu_options):
        if i == selected_index:
            stdscr.addstr(f"-> {option}\n")
        else:
            stdscr.addstr(f"   {option}\n")

def get_user_input(stdscr):
    stdscr.refresh()
    while True:
        key = stdscr.getch()
        return chr(key) if key < 256 else curses.keyname(key)


def menu(options):
    selected_index = 0
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    while True:
        stdscr.clear()
        print_menu(stdscr, options, selected_index)
        key = get_user_input(stdscr)

        if key == 'q':
            return None
        elif key == 'w' and selected_index > 0:
            selected_index -= 1
        elif key == 's' and selected_index < len(options) - 1:
            selected_index += 1
        elif key == 'enter' or key == '':
            return options[selected_index]


# Example usage
options = ["Option 1", "Option 2", "Option 3", "Quit"]
selected_option = menu(options)

