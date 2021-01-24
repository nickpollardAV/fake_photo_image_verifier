import json
from controller import controller



def respond(res):
    # print("CUSTOMER LOG")
    # print(json.dumps(res))
    return {
        'statusCode': 200,
        'body': json.dumps(res),
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin':'*'
        }
    }

def lambda_handler(event, context):
    print("TESTLOG")
    # controller(event)
    # return respond(event)