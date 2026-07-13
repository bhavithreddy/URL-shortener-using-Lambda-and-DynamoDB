import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('url-shortener')

def lambda_handler(event, context):
    try:
        short_code = event.get('pathParameters', {}).get('shortCode')

        if not short_code:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'Missing shortCode'})
            }

        response = table.get_item(Key={'shortCode': short_code})
        item = response.get('Item')

        if not item:
            return {
                'statusCode': 404,
                'headers': {'Content-Type': 'application/json'},
                'body': json.dumps({'error': 'Short URL not found'})
            }

        return {
            'statusCode': 301,
            'headers': {
                'Location': item['longUrl']
            },
            'body': ''
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }