import json
from controller import Controller



# def respond(res):
#     return {
#         'statusCode': 200,
#         'body': json.dumps(res),
#         'headers': {
#             'Content-Type': 'application/json',
#             'Access-Control-Allow-Origin':'*'
#         }
#     }

def lambda_handler(event, context):
    controller = Controller()
    controller.run_steps(event)