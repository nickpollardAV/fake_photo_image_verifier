from PIL import Image
import numpy as np

class ImageUtils():
    def convert_image_to_numbers_array(self, image_path):
        try:
            with Image.open(image_path) as image:
                rgb_im = image.convert('RGB')
                return np.array(rgb_im).flatten()
        except Exception as e:
            print(e)
    
    def convert_list_to_format_for_analysis(self, list_to_be_converted):
        return [int(str(number)[0]) for number in list_to_be_converted]


        