import json


def hello(event, context):
    body = {
        "message": event,
        "input": event
    }

    return {"statusCode": 200, "body": json.dumps(body)}
