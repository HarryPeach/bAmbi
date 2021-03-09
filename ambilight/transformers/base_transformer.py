from abc import ABC, abstractmethod
from ambilight.layout import Layout


class BaseTransformer(ABC):

    @abstractmethod
    def transform(self, layout: Layout):
        pass
