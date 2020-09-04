import json
import boto3
import os
import requests

SQS_URL = os.environ['SQS_URL']
sqsClient = boto3.client('sqs')

def doRequest(event, context):
    url = event.get("url")
    params = {'page': event.get("page")} 
    r = requests.get(url, params)
    data = r.json()
    return {
        "message": "Request is done.",
        "event": event,
        "data": data
    }

def retry(event, context):
    response = sqsClient.send_message(
        QueueUrl=SQS_URL,
        MessageBody=json.dumps(event),
        DelaySeconds=60*10,
    )
    return {
        "message": "Send SQS to retry",
        "event": event,
    }
    
