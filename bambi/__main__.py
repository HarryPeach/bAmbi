from bambi.renderers.terminal_renderer import TerminalRenderer
from bambi.renderers.serial_renderer import SerialRenderer
from bambi.transformers.average_colour_transformer import AverageColourTransformer
from bambi.transformers.snake_transformer import SnakeTransformer
from bambi.layout import Layout

import time

if __name__ == "__main__":
    layout = Layout((9, 6))

    time.sleep(5)

    act = AverageColourTransformer()
    serial_renderer = SerialRenderer()
    while True:
        act.transform(layout)

        ts = time.time()
        serial_renderer.render(layout)
        te = time.time()
        print(te - ts)
