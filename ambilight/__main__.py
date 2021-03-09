from ambilight.transformers.average_colour_transformer import AverageColourTransformer
from ambilight.renderers.terminal_renderer import TerminalRenderer
from ambilight.layout import Layout

if __name__ == "__main__":
    layout = Layout((8, 5))

    act = AverageColourTransformer()
    act.transform(layout)

    terminal_renderer = TerminalRenderer()
    terminal_renderer.render(layout)
