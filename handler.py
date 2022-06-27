import json

from create_tasks import create_task
from delete_tasks import delete_task
from get_tasks import get_task
from update_tasks import update_task


def hello(event, context):
    # event:  {'resource': '/create', 'httpMethod': 'POST', 'body': '{This data is useless}'}
    body = json.loads(event["body"])
    if event["httpMethod"] == "GET":
        return get_task(body)
    if event["httpMethod"] == "POST":
        return create_task(body)
    if event["httpMethod"] == "DELETE":
        return delete_task(body)
    if event["httpMethod"] == "PUT":
        return update_task(body)
