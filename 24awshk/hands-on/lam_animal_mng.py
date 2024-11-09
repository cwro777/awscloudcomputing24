import json
import boto3
import uuid
import logging

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Animals')
print('cwro check lambda Loading function')

def lambda_handler(event, context):
    logging.info("Received event: %s", event)

    http_method = event.get('httpMethod')
    if not http_method:
        return {
            'statusCode': 400,
            'body': json.dumps({'message': 'Invalid request, httpMethod missing'})
        }

    if http_method == 'POST':
        # 동물 추가
        body = json.loads(event['body'])
        animal_id = str(uuid.uuid4())
        animal = {
            'animalId': animal_id,
            'name': body['name'],
            'type': body['type'],
            'age': body['age']
        }
        table.put_item(Item=animal)
        return {
            'statusCode': 201,
            'body': json.dumps(animal)
        }
    
    elif http_method == 'GET':
        # 모든 동물 조회
        try:
            response = table.scan()
            items = response.get('Items', [])
            return {
                'statusCode': 200,
                'headers': {
                    'Content-Type': 'application/json',
                    'Access-Control-Allow-Origin': '*'  # CORS 설정
                },
                'body': json.dumps(items)
            }
        except Exception as e:
            return {
                'statusCode': 500,
                'body': json.dumps({'error': str(e)})
            }

    elif http_method == 'DELETE':
        # 동물 삭제
        animal_id = event['queryStringParameters']['animalId']
        table.delete_item(Key={'animalId': animal_id})
        return {
            'statusCode': 204,
            'body': ''
        }

    return {
        'statusCode': 400,
        'body': json.dumps({'message': 'Invalid request'})
    }
