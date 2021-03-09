from ambilight.layout import Layout
from expects import equal, expect


class TestLayout:
    def test_state_creation_size(self) -> None:
        """Tests that the layout state is of the correct size
        """
        layout = Layout((5, 3))
        expect(len(layout.top_state)).to(equal(5))
        expect(len(layout.bottom_state)).to(equal(5))
        expect(len(layout.left_state)).to(equal(3))
        expect(len(layout.right_state)).to(equal(3))

    def test_state_creation_default_state(self) -> None:
        """Tests that the default layout state is correctly initialized
        """
        layout = Layout((5, 5))
        ss = layout.get_stitched_state()
        for led in ss:
            expect(led).to(equal((0, 0, 0, 0)))
