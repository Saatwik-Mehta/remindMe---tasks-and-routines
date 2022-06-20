def create_task(event, context):


    # event:  {'resource': '/create', 'httpMethod': 'POST', 'body': '{This data is useless}'}

    return {"statusCode": 200, "body": "Successfully added the data"}
