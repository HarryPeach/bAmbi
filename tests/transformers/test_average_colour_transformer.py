from ambilight.transformers.average_colour_transformer import AverageColourTransformer
from ambilight.renderers.terminal_renderer import TerminalRenderer
from ambilight.layout import Layout
from unittest.mock import patch
from PIL import Image

from expects import expect, equal

class TestAverageColourTransformer():
    """Tests the AverageColourTransformer class
    """

    @patch("ambilight.transformers.average_colour_transformer.ImageGrab")
    def test_correct_average(self, mock_req):
        mock_req.grab.return_value = Image.open(
            "tests/transformers/resources/average_test_img.png")
        layout = Layout((2, 2))

        act = AverageColourTransformer()
        act.transform(layout)

        expected_output = [(255, 0, 0, 255), (0, 255, 0, 255), (0, 0, 255, 255), (255, 255, 0, 255), (0, 255, 255, 255), (255, 0, 255, 255), (0, 0, 0, 255), (255, 255, 255, 255)]
        expect(layout.get_stitched_state()).to(equal(expected_output))

        # tr = TerminalRenderer()
        # tr.render(layout)
