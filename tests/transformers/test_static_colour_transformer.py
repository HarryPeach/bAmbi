from ambilight.layout import Layout
from ambilight.transformers.static_colour_transformer import StaticColourTransformer
from expects import expect, equal


class TestStaticColourTransformer:
    def test_transform(self):
        """Tests that the transform correctly applies the same colour to all LEDs
        """
        layout = Layout((5, 5))
        colour = (255, 0, 255, 0)

        stc = StaticColourTransformer(colour=colour)
        stc.transform(layout)

        for led in layout.get_stitched_state():
            expect(led).to(equal(colour))
