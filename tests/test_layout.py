from bambi.layout import Layout
from expects import equal, expect, raise_error


class TestLayout:
    def test_state_creation_size(_) -> None:
        """Tests that the layout state is of the correct size
        """
        layout = Layout((5, 3))
        expect(len(layout.top_state)).to(equal(5))
        expect(len(layout.bottom_state)).to(equal(5))
        expect(len(layout.left_state)).to(equal(3))
        expect(len(layout.right_state)).to(equal(3))

    def test_state_creation_default_state(_) -> None:
        """Tests that the default layout state is correctly initialized
        """
        layout = Layout((5, 5))
        ss = layout.get_stitched_state()
        for led in ss:
            expect(led).to(equal((0, 0, 0)))

    def test_set_stitched_state(_) -> None:
        """Test that state can be created from a stitched state value
        """
        layout = Layout((2, 2))
        stitched_state = [(0, 0, 0), (1, 1, 1), (2, 2, 2),
                          (3, 3, 3), (4, 4, 4), (5, 5, 5), (6, 6, 6), (7, 7, 7)]

        layout.set_from_stitched_state(stitched_state)

        expect(layout.right_state).to(equal([(0, 0, 0), (1, 1, 1)]))
        expect(layout.top_state).to(equal([(2, 2, 2), (3, 3, 3)]))
        expect(layout.left_state).to(equal([(4, 4, 4), (5, 5, 5)]))
        expect(layout.bottom_state).to(equal([(6, 6, 6), (7, 7, 7)]))

    def test_set_stitched_state_invalid_count(_) -> None:
        """Test that state cannot be created from a stitched state that has too many or
        too few values
        """
        layout = Layout((2, 2))
        stitched_state_few = [(0, 0, 0), (1, 1, 1), (2, 2, 2),
                              (3, 3, 3), (4, 4, 4)]
        stitched_state_many = [(0, 0, 0), (1, 1, 1), (2, 2, 2),
                               (3, 3, 3), (4, 4, 4), (5, 5,
                                                      5), (6, 6, 6), (7, 7, 7),
                               (8, 8, 8)]

        expect(lambda: layout.set_from_stitched_state(
            stitched_state_few)).to(raise_error(ValueError))
        expect(lambda: layout.set_from_stitched_state(
            stitched_state_many)).to(raise_error(ValueError))
