import boto3

s3_client = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('employee3')

def lambda_handler(event, context):
	#list = []
	bucket = event['Records'][0]['s3']['bucket']['name']
	csv_file_name = event['Records'][0]['s3']['object']['key']
	#print(str(event))
	csv_object = s3_client.get_object(Bucket=bucket,Key=csv_file_name)
	csvFileReader = csv_object['Body'].read().decode("utf-8")

	#csvDict = csv.loads(csvFileReader)
	csv_data = csvFileReader.split("\n")

	print("csv_data =", csv_data)
	
	
	for data1 in csv_data:
		data = data1.split(",")
		print("data =", data)
		#print(str(data))
		#table.put_item(Item=data)
		table.put_item(
			Item= {"id": data[0],
			"Name": data[1],
			" Age":data[2],
			"Location":data[3]
			}
		)

	return 'put dynamodb table S3 bucket csv data through  Lambda'