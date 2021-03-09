"""Represents a layout of LEDs on the back of the monitor
"""


class Layout():
    def __init__(self, dimensions: tuple[int, int]) -> None:
        """Initializes the layout object

        Args:
            dimensions (tuple[int, int]): The dimensions of the led strips in x and y
        """
        # Set the initial state of all leds to black and dim
        self.led_state = [(0, 0, 0, 0)] * ((dimensions[0] + dimensions[1]) * 2)
