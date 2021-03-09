from ambilight.renderers.base_renderer import BaseRenderer


class GuiRenderer(BaseRenderer):

    def render(self, state: list[tuple(int, int, int, int)]):
        print(state)
