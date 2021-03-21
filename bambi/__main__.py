from bambi.renderers.terminal_renderer import TerminalRenderer
from bambi.renderers.serial_renderer import SerialRenderer
from bambi.transformers.average_colour_transformer import AverageColourTransformer
from bambi.layout import Layout

import time


def timeit(f):

    def timed(*args, **kw):

        ts = time.time()
        result = f(*args, **kw)
        te = time.time()

        print('func:%r args:[%r, %r] took: %2.4f sec' %
              (f.__name__, args, kw, te-ts))
        return result

    return timed


if __name__ == "__main__":
    layout = Layout((9, 6))

    time.sleep(5)

    act = AverageColourTransformer()
    for i in range(0, 30):
        ts = time.time()
        act.transform(layout)
        te = time.time()
        print(te - ts)


    # terminal_renderer = SerialRenderer()
    # terminal_renderer.render(layout)
