from typing import Dict

import boto3

dynamo_db = boto3.resource("dynamodb")
table = dynamo_db.Table("remind_me_table")


def get_task(data: Dict):
    """
    > This function gets a task from the database

    :param data: Dict
    :type data: Dict
    :return: The item is being returned.
    """

    resp = table.get_item(
        Key={
            "id": data["id"],
        }
    )
    item = resp["Item"]
    return item
