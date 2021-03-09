"""Represents a layout of LEDs on the back of the monitor
"""


class Layout():
    def __init__(self, dimensions: tuple[int, int]) -> None:
        """Initializes the layout object

        Args:
            dimensions (tuple[int, int]): The dimensions of the led strips in x and y
        """
        self.dimensions = dimensions
        # Set the initial state of all leds to black and dim
        self.top_state = self.bottom_state = [(0, 0, 0, 0)] * dimensions[0]
        self.left_state = self.right_state = [(0, 0, 0, 0)] * dimensions[1]

    def get_stitched_state(self) -> list[tuple[int, int, int, int]]:
        """Returns the state of all leds stitched together in the order of: top, right,
        bottom, left

        Returns:
            list[tuple[int, int, int, int]]: The stitched state
        """
        return self.top_state + self.right_state + self.bottom_state + self.left_state
