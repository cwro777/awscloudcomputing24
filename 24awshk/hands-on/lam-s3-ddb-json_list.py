import json
import boto3

s3_client = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('employee2')

def lambda_handler(event, context):
	#list = []
	bucket = event['Records'][0]['s3']['bucket']['name']
	json_file_name = event['Records'][0]['s3']['object']['key']
	#print(str(event))
	json_object = s3_client.get_object(Bucket=bucket,Key=json_file_name)
	jsonFileReader = json_object['Body'].read().decode("utf-8")
	jsonDict = json.loads(jsonFileReader)
	print(str(jsonDict))
	
	
	for people in jsonDict['person']:
	#for people in jsonDict:
		#print(str(people))
		table.put_item(Item=people)
	return 'put dynamodb table S3 bucket json data through  Lambda'