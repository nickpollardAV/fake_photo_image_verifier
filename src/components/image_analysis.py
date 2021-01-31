from src.utils.data_utils import DataUtils

class ImageAnalysis():
    def __init__(self):
        self.data_utils = DataUtils()

    def calculate_percentage_of_image_being_real(self, image_pixel_list):
        self.data_utils.convert_list_to_format_for_analysis(image_pixel_list)
