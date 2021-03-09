from bambi.renderers.terminal_renderer import TerminalRenderer
from expects import expect, equal


class TestTerminalRenderer():
    def test_rgba_to_hex(self):
        tr = TerminalRenderer()

        expect(tr._rgba_to_hex((255, 0, 0, 0))).to(equal("#ff0000"))
        expect(tr._rgba_to_hex((0, 255, 0, 0))).to(equal("#00ff00"))
        expect(tr._rgba_to_hex((0, 0, 255, 0))).to(equal("#0000ff"))
        expect(tr._rgba_to_hex((0, 0, 0, 0))).to(equal("#000000"))
        expect(tr._rgba_to_hex((123, 85, 23, 0))).to(equal("#7b5517"))
