from abc import ABC, abstractmethod


class BaseTransformer(ABC):

    @abstractmethod
    def transform(self, state: list[tuple(int, int, int, int)]):
        pass
