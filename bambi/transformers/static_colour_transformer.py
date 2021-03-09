from bambi.transformers.base_transformer import BaseTransformer
from bambi.layout import Layout


class StaticColourTransformer(BaseTransformer):

    def __init__(self, colour: tuple[int, int, int, int]) -> None:
        self.colour = colour

    def transform(self, layout: Layout) -> None:
        states = [layout.top_state, layout.right_state,
                  layout.bottom_state, layout.left_state]
        for state in states:
            state[:] = [self.colour for _ in state]
