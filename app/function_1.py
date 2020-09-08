import json
import boto3
import os

SQS_URL = os.environ['SQS_URL']
client = boto3.client('sqs')

ssm = boto3.client('ssm')
params = ssm.get_parameters_by_path(
    Path='/teste/endpoints/',
    Recursive=True,
    WithDecryption=False
)

def postEndpoints(event, context):
    print({ "PARAMS": params })
    for p in params.get("Parameters"):
        print({ "EACH": p })
        endpointParam = json.loads(p.get("Value"))
        endpointParam['count'] = 1
        print(endpointParam)
        response = client.send_message(
            QueueUrl=SQS_URL,
            MessageBody=json.dumps(endpointParam),
            DelaySeconds=5,
        )
    return {
        "message": "Your function executed successfully!",
        "event": event,
    }
    
