from unittest import mock, TestCase
from unittest.mock import patch

from src.components.image_analysis import ImageAnalysis
from src.utils.data_utils import DataUtils

class ImageAnalysisTest(TestCase):

    def test_calculate_percentage_of_image_being_real_function_calls_convert_list_to_format_for_analysis_function(self):
        image_analysis = ImageAnalysis()
        with patch.object(DataUtils, 'convert_list_to_format_for_analysis') as mock:
            image_analysis.calculate_percentage_of_image_being_real("image")
        
        mock.assert_called_with("image")
