from bambi.layout import Layout
from bambi.transformers.base_transformer import BaseTransformer
from PIL import Image, ImageDraw, ImageGrab
import random


class AverageColourTransformer(BaseTransformer):

    def _draw_box(self, img, bb_width, bb_height, start_x, start_y) -> str:
        imd = ImageDraw.Draw(img)
        cropped_image = img.crop((start_x, start_y, start_x + bb_width,
                                  start_y + bb_height))
        cropped_image.thumbnail((1, 1), Image.NEAREST)
        color = cropped_image.getpixel((0, 0))

        imd.rectangle([(start_x, start_y), (start_x + bb_width,
                                            start_y + bb_height)],
                      fill=color, outline="#000000")

        return color + (255,)

    def transform(self, layout: Layout) -> None:
        im = ImageGrab.grab()

        bounding_box_width = im.width / (layout.dimensions[0] + 2)
        bounding_box_height = im.height / (layout.dimensions[1] + 2)

        for i in range(len(layout.top_state)):
            start_x = (i + 1) * bounding_box_width
            start_y = 0
            layout.top_state[i] = self._draw_box(im, bounding_box_width,
                                                 bounding_box_height, start_x, start_y)

        for i in range(len(layout.right_state)):
            start_x = im.width - bounding_box_width
            start_y = (i + 1) * bounding_box_height
            layout.right_state[i] = self._draw_box(im, bounding_box_width,
                                                   bounding_box_height, start_x, start_y)

        for i in range(len(layout.bottom_state)):
            # ir reverses the order of the colours
            ir = len(layout.bottom_state) - 1 - i
            start_x = (ir + 1) * bounding_box_width
            start_y = im.height - bounding_box_height
            layout.bottom_state[i] = self._draw_box(im, bounding_box_width,
                                                    bounding_box_height, start_x, start_y)

        for i in range(len(layout.left_state)):
            # ir reverses the order of the colours
            ir = len(layout.left_state) - 1 - i
            start_x = 0
            start_y = (ir + 1) * bounding_box_height
            layout.left_state[i] = self._draw_box(im, bounding_box_width,
                                                  bounding_box_height, start_x, start_y)

        # im.show()
