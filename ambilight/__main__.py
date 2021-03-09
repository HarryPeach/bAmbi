from ambilight.renderers.terminal_renderer import TerminalRenderer

if __name__ == "__main__":
    terminal_renderer = TerminalRenderer()
    terminal_renderer.render([(255, 0, 0, 0), (0, 255, 0, 0)])
