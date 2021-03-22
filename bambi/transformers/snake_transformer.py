from bambi.layout import Layout
from bambi.transformers.base_transformer import BaseTransformer


class SnakeTransformer(BaseTransformer):

    def __init__(self) -> None:
        self.index = 0

    def transform(self, layout: Layout) -> None:
        layout_stitched = layout.get_stitched_state()

        for i in range(len(layout_stitched)):
            layout_stitched[i] = (0, 0, 0)

        layout_stitched[self.index] = (255, 255, 255)
        layout.set_from_stitched_state(layout_stitched)

        if (self.index == len(layout_stitched) - 1):
            self.index = 0
        else:
            self.index = self.index + 1
