import readchar
import rich.panel
from rich.console import Console, ConsoleRenderable
from rich.layout import Layout
from rich.live import Live
from rich.panel import Panel
from rich.style import Style
from rich.text import Text


class MenuOption:
    def __init__(self, text: str, color: rich.style.Color = rich.style.Color.from_rgb(255, 255, 255),
                 background: rich.style.Color = rich.style.Color.from_rgb(0, 0, 0), sub_menu=None):
        self.sub_menu = sub_menu if sub_menu is not None else []
        self.text = text
        self.color = color
        self.background = background


def options_from_str_list(str_list: list[str]) -> list[MenuOption]:
    return [MenuOption(v) for v in str_list]


class Printer:
    def __init__(self):
        self.console = Console()

    def println(self, txt: str):
        self.console.print(txt)

    def wait(self):
        self.console.input()

    def clear(self):
        self.console.clear()

    def menu_panel(self, options: list[MenuOption], selected_index, selected):
        menu_items = [
            Text(f"{'> ' if i == selected_index and selected else '  '}{option.text}",
                 style=Style(color="red", bold=True) if i == selected_index
                 else Style(color=option.color, bgcolor=option.background))
            for i, option in enumerate(options)
        ]

        menu_panel = Panel("\n".join(str(item) for item in menu_items))
        return menu_panel

    def display_menu(self, options: list[MenuOption], selected_index, sub_selected) -> ConsoleRenderable:
        has_sub = len(options[selected_index].sub_menu) > 0
        menu_panel = self.menu_panel(options, selected_index, sub_selected == - 1)
        if has_sub:
            sub_menu_panel = self.menu_panel(options[selected_index].sub_menu, sub_selected, sub_selected != -1)
            menu_layout = Layout()
            menu_layout.split_row(
                Layout(menu_panel),
                Layout(sub_menu_panel)
            )
            return menu_layout
        return menu_panel

    def menu(self, options: list[MenuOption], layout: Layout | None = None) -> (int, int):
        selected_index = 0
        sub_selected = -1

        max_size = len(options)

        for option in options:
            the_len = len(option.sub_menu)
            if the_len > max_size:
                max_size = the_len

        if layout is None:
            layout = Layout()
            layout.split_column(
                Layout(name="menu", size=max_size + 2),
            )

        with Live(layout, console=self.console, auto_refresh=True) as live:
            while True:
                key = readchar.readkey()

                if key == readchar.key.UP:
                    if sub_selected == -1:
                        selected_index -= 1 if selected_index > 0 else 0
                    else:
                        sub_selected -= 1 if sub_selected > 0 else 0
                elif key == readchar.key.DOWN:
                    if sub_selected == -1:
                        selected_index += 1 if selected_index < len(options) - 1 else 0
                    else:
                        sub_selected += 1 if sub_selected < len(options[selected_index].sub_menu) - 1 else 0
                elif key == readchar.key.RIGHT:
                    if len(options[selected_index].sub_menu) > 0:
                        sub_selected = 0 if sub_selected == -1 else sub_selected
                elif key == readchar.key.LEFT:
                    sub_selected = -1
                elif key in (readchar.key.ENTER, '\r', '\n'):
                    return selected_index, sub_selected
                elif key in (readchar.key.CTRL_C, readchar.key.ESC):
                    return -1, -1

                menu_content = self.display_menu(options, selected_index, sub_selected)
                layout["menu"].update(menu_content)
                live.refresh()
