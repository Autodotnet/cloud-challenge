import boto3 # type: ignore

# Define the DynamoDB table that Lambda will connect to
table_name = "lambda-apigateway"

# Create the DynamoDB resource
dynamo = boto3.resource('dynamodb').Table(table_name)

# Define some functions to perform the CRUD operations
def read(payload):
    return dynamo.get_item(Key=payload['Key'])

operations = {'read': read}

def lambda_handler(event, context):
    operation = event['operation']
    payload = event['payload']
    
    if operation in operations:
        return operations[operation](payload)
        
    else:
        raise ValueError(f'Unrecognized operation "{operation}"')
    