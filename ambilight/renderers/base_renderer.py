from abc import ABC, abstractmethod


class BaseRenderer(ABC):

    @abstractmethod
    def render(self, state: list[tuple(int, int, int, int)]):
        pass
