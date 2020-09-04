import json
import boto3
import os

SQS_URL = os.environ['SQS_URL']
client = boto3.client('sqs')

def postEndpoints(event, context):
    for e in event:
        response = client.send_message(
            QueueUrl=SQS_URL,
            MessageBody=json.dumps(e),
            DelaySeconds=5,
        )
    return {
        "message": "Your function executed successfully!",
        "event": event,
    }
    
