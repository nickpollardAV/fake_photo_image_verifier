# import boto3
# import os
# import sys
# import uuid
# from urllib3.parse import unquote_plus
# from PIL import Image
# import PIL.Image

# def controller(event):
#     for record in event['Records']:
#         bucket = record['s3']['bucket']['name']
#         key = unquote_plus(record['s3']['object']['key'])
        # tmpkey = key.replace('/', '')
        # download_path = '/tmp/{}{}'.format(uuid.uuid4(), tmpkey)
        # s3_client.download_file(bucket, key, download_path)
        # temp_read_image(download_path)



import json
import urllib.parse
import boto3
import os
import sys
import uuid
from urllib.parse import unquote_plus
from PIL import Image
import PIL.Image

print('Loading function')

s3 = boto3.client('s3')


def controller(event):
    #print("Received event: " + json.dumps(event, indent=2))

    # Get the object from the event and show its content type
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    tmpkey = key.replace('/', '')
    download_path = '/tmp/{}{}'.format(uuid.uuid4(), tmpkey)
    s3.download_file(bucket, key, download_path)
    temp_read_image(download_path)
    try:
        response = s3.get_object(Bucket=bucket, Key=key)
        print(response)
        print("CONTENT TYPE: " + response['ContentType'])
        return response['ContentType']
    except Exception as e:
        print(e)
        print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(key, bucket))
        raise e

def temp_read_image(image_path):
    with Image.open(image_path) as image:
        pixels = list(image.getdata())
        print(pixels)
