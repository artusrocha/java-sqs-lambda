import json
import boto3
import os
#import requests

SQS_URL = os.environ['SQS_URL']
sqsClient = boto3.client('sqs')

def doRequests(event, context):
    url = event.get("url")
    params = {'page': event.get("page")} 
    #r = requests.get(url, params)
    #data = r.json()
    out = {
        "message": "Request is done.",
        "event": event,
#        "data": data
    }
    print(out)
    return out

def retry(event, context):
    response = sqsClient.send_message(
        QueueUrl=SQS_URL,
        MessageBody=json.dumps(event),
        DelaySeconds=60*10,

    )
    out = {
        "message": "Send SQS to retry",
        "event": event,
    }
    print(out)
    return out
    
