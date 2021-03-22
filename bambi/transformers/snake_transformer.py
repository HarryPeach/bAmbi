from bambi.layout import Layout
from bambi.transformers.base_transformer import BaseTransformer


class SnakeTransformer(BaseTransformer):

    def __init__(self) -> None:
        self.index = 0

    def transform(self, layout: Layout) -> None:
        # layout_cp = layout.bottom_state.copy()
        for i, led in enumerate(layout.bottom_state):
            layout.bottom_state[i] = (255, 0, 0)
        # layout.bottom_state[:] = layout_cp
