from ambilight.layout import Layout
from expects import equal, expect


class TestLayout:
    def test_state_creation_size(self) -> None:
        """Tests that the layout state is of the correct size
        """
        expect(len(Layout((5, 3)).led_state)).to(equal(16))
        expect(len(Layout((7, 1)).led_state)).to(equal(16))
        expect(len(Layout((9, 3)).led_state)).to(equal(24))

    def test_state_creation_default_state(self) -> None:
        """Tests that the default layout state is correctly initialized
        """
        layout = Layout((5, 5))
        for led in layout.led_state:
            expect(led).to(equal((0, 0, 0, 0)))
