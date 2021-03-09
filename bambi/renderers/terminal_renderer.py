from bambi.renderers.base_renderer import BaseRenderer
from bambi.layout import Layout
from colored import bg, attr

import os


class TerminalRenderer(BaseRenderer):
    def __init__(self) -> None:
        self.led_draw_state = None

    def _rgba_to_hex(self, rgba: tuple[int, int, int, int]) -> str:
        """Converts an rgba value to its hex equivalent

        Args:
            rgba (tuple[int, int, int, int]): The rgba value to process

        Returns:
            str: The hexadecimal string value
        """
        return "#%02x%02x%02x" % (max(0, min(rgba[0], 255)), max(0, min(rgba[1], 255)),
                                  max(0, min(rgba[2], 255)))

    def render(self, layout: Layout) -> None:
        PRINT_CHAR = " "
        os.system('cls' if os.name == 'nt' else 'clear')

        print(bg("#000000") + PRINT_CHAR, end="")
        for item in layout.top_state:
            print(bg(self._rgba_to_hex(item)) + PRINT_CHAR, end="")
        print(bg("#000000") + PRINT_CHAR, end="")
        print(attr("reset"))

        for i in range(len(layout.left_state)):
            print(bg(self._rgba_to_hex(
                layout.left_state[i])) + PRINT_CHAR, end="")
            for _ in range(len(layout.top_state)):
                print(bg("#000000") + PRINT_CHAR, end="")
            print(bg(self._rgba_to_hex(
                layout.right_state[i])) + PRINT_CHAR, end="")
            print(attr("reset"))

        print(bg("#000000") + PRINT_CHAR, end="")
        for item in reversed(layout.bottom_state):
            print(bg(self._rgba_to_hex(item)) + PRINT_CHAR, end="")
        print(bg("#000000") + PRINT_CHAR, end="")
        print(attr("reset"))
