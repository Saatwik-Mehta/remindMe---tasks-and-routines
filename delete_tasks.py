"""
Use to delete the tasks from db
{"id": int}
"""
from typing import Dict

import boto3

dynamo_db = boto3.resource("dynamodb")
table = dynamo_db.Table("remind_me_table")


def delete_task(data: Dict):
    """
    It deletes an item from the DynamoDB table

    :param data: Dict - This is the data that is passed to the function
    :type data: Dict
    :return: The status code 204 is being returned.
    """

    table.delete_item(
        Key={
            "id": data["id"],
        }
    )
    return {"statusCode": 204, "body": "Item deleted successfully"}
