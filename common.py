"""
This file will contain all the function that are common to the project
"""
import logging
import boto3

LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.INFO)


ses_client = boto3.client("ses")


def send_email(
    sender="saatwikmehta@gmail.com",
    to="saatwikmehta@gmail.com",
    sub="",
    text="",
):
    """
    This function sends an email to the specified email address

    :param sender: The email address of the sender, defaults to saatwikmehta@gmail.com (optional)
    :param to: The email address of the recipient, defaults to saatwik@codeops.tech (optional)
    :param sub: Subject of the email
    :param text: The body of the email
    (optional)
    """
    Source = sender
    Destination = {
        "ToAddresses": [to],
    }
    Message = {"Subject": {"Data": sub}, "Body": {"Text": {"Data": text}}}
    logging.info(
        "Following inputs were given:\n Source: %s\nDestination: %s\nMessage: %s\nReplyToAddresses: %s",
        sender,
        Destination,
        Message,
    )
    ses_client.send_email(
        Source=Source,
        Destination=Destination,
        Message=Message,
    )
