from abc import ABC, abstractmethod
from bambi.layout import Layout


class BaseTransformer(ABC):

    @abstractmethod
    def transform(self, layout: Layout):
        pass
