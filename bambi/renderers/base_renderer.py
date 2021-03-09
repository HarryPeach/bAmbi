from abc import ABC, abstractmethod


class BaseRenderer(ABC):

    @abstractmethod
    def render(self, state: list[tuple[int, int, int, int]]):
        """Renders the led state to the chosen medium

        Args:
            state (list[tuple[int, int, int, int]]): The LED state to render
        """
        pass
