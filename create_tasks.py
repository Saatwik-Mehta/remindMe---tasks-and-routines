"""
Used to create new tasks
data: {
"id": int,
"task":"Something goes here",
"schedule": time,
"created_at": time
}
"""
import logging
from typing import Dict
import boto3

from common import send_email

dynamo_db = boto3.resource("dynamodb", "ap-south-1")
table = dynamo_db.Table("remind_me_table")

LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.INFO)


def create_task(data: Dict):
    """
    It takes a dictionary as input, and adds it to the DynamoDB table

    :param data: Dict - This is the data that we're going to pass to the function
    :type data: Dict
    :return: A dictionary with a status code and a body.
    """
    LOGGER.info("/////////////////input_data: %s", data)
    if "id" not in data:
        LOGGER.info("Missing mandatory column: id")
        return dict(statusCode=400, error="missing column: id")
    table.put_item(
        Item=data,
    )
    send_mail_to_user()
    return {"statusCode": 200, "body": "Item added successfully"}


def send_mail_to_user():
    """
    This function simply sends an email to the task
    creator confirming the task has been created and scheduled for the time being
    """
    text = (
        "Your task has been created and scheduled successfully."
        " It will be reminded to you on time with email!"
        " Thanks for using our services."
    )
    subject = "Confirmation of the task creation"
    send_email(sub=subject, text=text)
