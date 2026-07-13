import json
import boto3
import string
import random
import os

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('url-shortener')

BASE_URL = os.environ.get('BASE_URL', 'https://your-api-id.execute-api.ap-south-1.amazonaws.com/prod')

def generate_code(length=6):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choices(chars, k=length))

def lambda_handler(event, context):
    try:
        body = json.loads(event.get('body', '{}'))
        long_url = body.get('url')

        if not long_url:
            return {
                'statusCode': 400,
                'headers': {'Content-Type': 'application/json'},
                'body': json.dumps({'error': 'Missing url in request body'})
            }

        short_code = generate_code()

        table.put_item(Item={
            'shortCode': short_code,
            'longUrl': long_url
        })

        return {
            'statusCode': 200,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps({
                'shortUrl': f'{BASE_URL}/{short_code}',
                'shortCode': short_code
            })
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps({'error': str(e)})
        }