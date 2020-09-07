import json
import boto3
import os

SQS_URL = os.environ['SQS_URL']
client = boto3.client('sqs')

sample = [{
    "url": "https://reqres.in/api/users",
    "page": 1,
    "count": 1,
    "foo": "bar",
}]

def postEndpoints(event, context):
    print("Event: ")
    print(event)
    print("##########################")
    for e in sample:
        response = client.send_message(
            QueueUrl=SQS_URL,
            MessageBody=json.dumps(e),
            DelaySeconds=5,
        )
    return {
        "message": "Your function executed successfully!",
        "event": event,
    }
    
