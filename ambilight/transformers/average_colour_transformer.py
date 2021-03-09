from ambilight.layout import Layout
from ambilight.transformers.base_transformer import BaseTransformer
from PIL import Image, ImageDraw, ImageGrab
import random


class AverageColourTransformer(BaseTransformer):

    def _get_random_color(self) -> str:
        return "#"+''.join([random.choice('0123456789ABCDEF')
                            for _ in range(6)])

    def transform(self, layout: Layout) -> None:
        im = ImageGrab.grab()

        bounding_box_width = im.width / (layout.dimensions[0] + 2)
        bounding_box_height = im.height / (layout.dimensions[1] + 2)
        print(bounding_box_width)

        img = ImageDraw.Draw(im)

        for i in range(len(layout.top_state)):
            start_x = (i + 1) * bounding_box_width
            start_y = 0
            img.rectangle([(start_x, start_y), (start_x + bounding_box_width,
                                                start_y + bounding_box_height)],
                          fill=self._get_random_color(), outline="#ff0000")

        for i in range(len(layout.bottom_state)):
            start_x = (i + 1) * bounding_box_width
            start_y = im.height - bounding_box_height
            img.rectangle([(start_x, start_y), (start_x + bounding_box_width,
                                                im.height)],
                          fill=self._get_random_color(), outline="#ff0000")

        for i in range(len(layout.right_state)):
            start_x = im.width - bounding_box_width
            start_y = (i + 1) * bounding_box_height
            img.rectangle([(start_x, start_y), (start_x + bounding_box_width,
                                                start_y + bounding_box_height)],
                          fill=self._get_random_color(), outline="#ff0000")

        for i in range(len(layout.left_state)):
            start_x = 0
            start_y = (i + 1) * bounding_box_height
            img.rectangle([(start_x, start_y), (start_x + bounding_box_width,
                                                start_y + bounding_box_height)],
                          fill=self._get_random_color(), outline="#ff0000")

        im.show()
