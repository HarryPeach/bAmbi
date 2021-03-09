from ambilight.renderers.base_renderer import BaseRenderer

from colored import bg, attr


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

    def render(self, state: list[tuple[int, int, int, int]]) -> None:
        for item in state:
            print(bg(self._rgba_to_hex(item)) + "#", end="")
        print(attr("reset"))
