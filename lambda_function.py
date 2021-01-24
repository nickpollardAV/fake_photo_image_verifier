# import json
# from src.controller import controller



# def respond(res):
#     # print("CUSTOMER LOG")
#     # print(json.dumps(res))
#     return {
#         'statusCode': 200,
#         'body': json.dumps(res),
#         'headers': {
#             'Content-Type': 'application/json',
#             'Access-Control-Allow-Origin':'*'
#         }
#     }

# def lambda_handler(event, context):
#     print("INVOKED")
#     print("INVOKED")
#     # controller(event)
#     # return respond(event)


# import json
# import urllib.parse
# import boto3

# print('Loading function')

# s3 = boto3.client('s3')


# def lambda_handler(event, context):
#     #print("Received event: " + json.dumps(event, indent=2))

#     # Get the object from the event and show its content type
#     bucket = event['Records'][0]['s3']['bucket']['name']
#     key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
#     try:
#         response = s3.get_object(Bucket=bucket, Key=key)
#         print("CONTENT TYPE: " + response['ContentType'])
#         return response['ContentType']
#     except Exception as e:
#         print(e)
#         print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(key, bucket))
#         raise e