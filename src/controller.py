
import boto3
import os
import sys
import uuid
from urllib.parse import unquote_plus
from PIL import Image
# import PIL.Image
# import pillow
from utils.image_utils import ImageUtils

s3_client = boto3.client('s3')

class Controller():

    def __init__(self):
        self.image_utils = ImageUtils()

    def run_steps(self, event):
        for record in event['Records']:
            try:
                bucket = record['s3']['bucket']['name']
                key = unquote_plus(record['s3']['object']['key'])
                tmpkey = key.replace('/', '')
                download_path = '/tmp/{}{}'.format(uuid.uuid4(), tmpkey)
                s3_client.download_file(bucket, key, download_path)
                image_numbers_list = self.image_utils.convert_image_to_numbers_array(download_path)
                print(image_numbers_list)

            except Exception as e:
                # this exception will need to be modified
                print(e)
                print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(key, bucket))
                raise e

