from unittest import mock, TestCase

from PIL import Image

from src.utils.data_utils import DataUtils

class DataUtilsTest(TestCase):

    def setUp(self):
        self.data_utils = DataUtils()

    def test_convert_list_to_format_for_analysis_returns_list_in_where_only_first_digit_of_list_item_is_present(self):
        result = self.data_utils.convert_list_to_format_for_analysis([203,305,406])

        self.assertEqual(result, [2,3,4])

if __name__ == '__main__':
    unittest.main()
            
