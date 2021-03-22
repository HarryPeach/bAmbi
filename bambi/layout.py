from itertools import islice

"""Represents a layout of LEDs on the back of the monitor
"""


class Layout():
    def __init__(self, dimensions: tuple[int, int]) -> None:
        """Initializes the layout object

        Args:
            dimensions (tuple[int, int]): The dimensions of the led strips in x and y
        """
        self.dimensions = dimensions
        # Set the initial state of all leds to black (off)
        self.top_state = [(0, 0, 0)] * dimensions[0]
        self.bottom_state = [(0, 0, 0)] * dimensions[0]
        self.left_state = [(0, 0, 0)] * dimensions[1]
        self.right_state = [(0, 0, 0)] * dimensions[1]

    def get_stitched_state(self) -> list[tuple[int, int, int]]:
        """Returns the state of all leds stitched together in the order of: top, right,
        bottom, left

        Returns:
            list[tuple[int, int, int, int]]: The stitched state
        """
        return self.right_state + self.top_state + self.left_state + self.bottom_state

    def set_from_stitched_state(self, stitched_state: list[tuple[int, int, int]]):
        """Sets the layout from a stitched state

        Args:
            list (tuple[int, int, int]): The stitched state to "de-stitch"
        """
        if len(stitched_state) != (self.dimensions[0] + self.dimensions[1]) * 2:
            raise ValueError("Stitched state was of incorrect size")

        chunk_sizes = [self.dimensions[0], self.dimensions[1],
                       self.dimensions[0], self.dimensions[1]]

        it = iter(stitched_state)
        sliced_states = [list(islice(it, 0, i)) for i in chunk_sizes]

        self.right_state = sliced_states[0]
        self.top_state = sliced_states[1]
        self.left_state = sliced_states[2]
        self.bottom_state = sliced_states[3]
