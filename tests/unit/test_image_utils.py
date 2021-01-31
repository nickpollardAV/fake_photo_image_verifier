from unittest import mock, TestCase
from unittest.mock import patch

from PIL import Image
from io import BytesIO
import numpy as np

from src.utils.image_utils import ImageUtils

class UtilsTest(TestCase):

    def setUp(self):
        self.ImageUtils = ImageUtils()

    def create_test_image(self):
        # https://wildfish.com/blog/2014/02/27/generating-in-memory-image-for-tests-python/
        file = BytesIO()
        image = Image.new('RGBA', size=(2, 2), color=(155, 0, 0))
        image.save(file, 'png')
        file.name = 'test.png'
        file.seek(0)
        return file

    def test_convert_image_to_numbers_array_opens_image_from_download_path(self):
        with patch.object(Image, 'open') as mock:
            self.ImageUtils.convert_image_to_numbers_array("test_path")
        
        mock.assert_called_with("test_path")

    def test_convert_image_to_numbers_array_converts_image_to_rbg_array(self):
        test_file_location = self.create_test_image()
        
        result = self.ImageUtils.convert_image_to_numbers_array(test_file_location)
     
        np.testing.assert_array_equal(result, np.array([155, 0, 0, 155, 0, 0, 155, 0, 0, 155, 0, 0]))

if __name__ == '__main__':
    unittest.main()
            
