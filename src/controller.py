
import boto3
import os
import sys
import uuid
from urllib.parse import unquote_plus
from PIL import Image
import PIL.Image

s3_client = boto3.client('s3')

def controller(event):
    for record in event['Records']:
        try:
            bucket = record['s3']['bucket']['name']
            key = unquote_plus(record['s3']['object']['key'])
            tmpkey = key.replace('/', '')
            download_path = '/tmp/{}{}'.format(uuid.uuid4(), tmpkey)
            s3_client.download_file(bucket, key, download_path)
            temp_read_image(download_path)
        except Exception as e:
            print(e)
            print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(key, bucket))
            raise e


def temp_read_image(image_path):
    with Image.open(image_path) as image:
        rgb_im = image.convert('RGB')
        r, g, b = rgb_im.getpixel((1, 1))

        print(r, g, b)