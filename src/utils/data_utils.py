from PIL import Image
import numpy as np

class DataUtils():    
    def convert_list_to_format_for_analysis(self, list_to_be_converted):
        return [int(str(number)[0]) for number in list_to_be_converted]
