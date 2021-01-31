from PIL import Image
import numpy as np

class ImageUtils():
    def convert_image_to_numbers_array(self, image_path):
        with Image.open(image_path) as image:
            rgb_im = image.convert('RGB')
       
            return np.array(rgb_im).flatten()

        