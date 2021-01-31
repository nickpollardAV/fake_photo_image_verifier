from PIL import Image

class ImageUtils():
    def convert_image_to_numbers_list(self, image_path):
        with Image.open(image_path) as image:
            pass
            # rgb_im = image.convert('RGB')
            # r, g, b = rgb_im.getpixel((1, 1))
            # print(r,g,b)
        