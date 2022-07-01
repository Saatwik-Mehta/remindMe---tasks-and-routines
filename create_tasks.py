from typing import Dict
import boto3

dynamo_db = boto3.resource("dynamodb")
table = dynamo_db.Table("remind_me_table")


def create_task(data: Dict):
    """
    It takes a dictionary as input, and adds it to the DynamoDB table

    :param data: Dict - This is the data that we're going to pass to the function
    :type data: Dict
    :return: A dictionary with a status code and a body.
    """

    table.put_item(
        Item=data,
    )

    return {"statusCode": 200, "body": "Item added successfully"}
