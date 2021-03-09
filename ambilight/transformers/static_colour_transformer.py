from ambilight.transformers.base_transformer import BaseTransformer


class StaticColourTransformer(BaseTransformer):

    def __init__(self, colour: tuple[int, int, int, int]) -> None:
        self.colour = colour

    def transform(self, state: list[tuple[int, int, int, int]]) -> None:
        new_state = [self.colour for _ in state]
        state[:] = new_state
