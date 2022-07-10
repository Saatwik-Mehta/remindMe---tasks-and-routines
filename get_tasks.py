"""
This module is used to Fetch the available tasks from the Db
"""
import boto3

dynamo_db = boto3.resource("dynamodb")
table = dynamo_db.Table("remind_me_table")


def get_task():
    """
    > This function get all the tasks from the database
    :return: The item is being returned.
    """

    resp = table.scan()
    items = resp["Items"]
    return items
