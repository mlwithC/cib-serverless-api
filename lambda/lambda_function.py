import json
import boto3
import uuid

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Messages')

def lambda_handler(event, context):

    body = json.loads(event['body'])

    item = {
        'messageId': str(uuid.uuid4()),
        'name': body['name'],
        'message': body['message']
    }

    table.put_item(Item=item)

    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps({
            'message': 'Message saved successfully'
        })
    }