import serial

from bambi.renderers.base_renderer import BaseRenderer
from bambi.layout import Layout


class SerialRenderer(BaseRenderer):

    def __init__(self) -> None:
        self.serial = serial.Serial("COM5", 115200)

    def render(self, layout: Layout) -> None:
        for i, led in enumerate(layout.get_stitched_state()):
            self.serial.write(f"{i}:{led[0]},{led[1]},{led[2]};".encode())

    def __del__(self) -> None:
        self.serial.close()
