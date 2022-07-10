"""
Used to connect all the lambda functions into a file
ALL CRUD operations are mentioned here
"""

import json
from create_tasks import create_task
from delete_tasks import delete_task
from get_tasks import get_task
from update_tasks import update_task


def hello(event, context):
    if event.get("body"):
        body = json.loads(event["body"])
    if event["requestContext"]["http"]["method"] == "GET":
        return get_task()
    if event["requestContext"]["http"]["method"] == "POST":
        return create_task(body)
    if event["requestContext"]["http"]["method"] == "DELETE":
        return delete_task(body)
    if event["requestContext"]["http"]["method"] == "PUT":
        return update_task(body)
    return None
