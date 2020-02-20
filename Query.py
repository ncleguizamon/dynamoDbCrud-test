import boto3
from boto3.dynamodb.conditions import Key, Attr

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('staff')

response = table.query(
    KeyConditionExpression=Key('username').eq('ruanb') & Key('last_name').eq('bekker')
)

items = response['Items']
print(items)