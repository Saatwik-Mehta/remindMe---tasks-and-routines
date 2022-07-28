"""
Used to update the tasks in the db
updated_data: {
"id": int,
"task":"Something updated goes here",
"schedule": time,
"created_at": time
}
"""
from typing import Dict

import boto3

from common import send_email

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


def send_mail_to_user():
    """
    This function simply sends an email to the task
    updater confirming the task has been updated"""
    text = "Your task has been updated successfully."
    subject = "Confirmation of the task creation"
    send_email(sub=subject, text=text)
