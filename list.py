import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('staff')

response = table.get_item(
   Key={
        'username': 'stefanb',
        'last_name': 'bester'
  }
)

item = response['Item']
name = item['first_name']

print(item)
print("Hello, {}" .format(name))