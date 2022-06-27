from typing import Dict

import boto3

dynamo_db = boto3.resource("dynamodb")
table = dynamo_db.Table("remind_me_table")


def update_task(data: Dict):
    """
    It takes a dictionary of data, and puts it into the DynamoDB table

    :param data: Dict
    :type data: Dict
    :return: A dictionary with a status code and a body.
    """

    table.put_item(
        Item=data,
    )

    return {"statusCode": 200, "body": "Item updated successfully"}
