import logging
import boto3
import json
import os



session = boto3.Session(region_name=os.environ['REGION'])
dynamodb_client = session.client('dynamodb')

def lambda_handler(event, context):
    try:
        print("event ->" + str(event))
        payload = json.loads(event["body"])
        print("payload ->" + str(payload))
        dynamodb_response = dynamodb_client.get_item(
            TableName=os.environ["PRODUCT_TABLE"],
            Item={
                "product_id": {
                    "S": payload["productId"]
                }
            }
        )
        print(dynamodb_response)
        return {
            'statusCode': 201,
           'body': '{"status":"Product created"}'
        }
    except Exception as e:
        logging.error(e)
        return {
            'statusCode': 500,
           'body': '{"status":"Server error"}'
        }