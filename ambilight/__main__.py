from ambilight.transformers.average_colour_transformer import AverageColourTransformer
from ambilight.renderers.terminal_renderer import TerminalRenderer
from ambilight.layout import Layout

from time import sleep

if __name__ == "__main__":
    layout = Layout((8, 5))

    sleep(4)

    act = AverageColourTransformer()
    act.transform(layout)

    terminal_renderer = TerminalRenderer()
    terminal_renderer.render(layout)
