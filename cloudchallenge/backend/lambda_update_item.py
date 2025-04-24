import boto3 # type: ignore

# Define the DynamoDB table that Lambda will connect to
table_name = "lambda-apigateway"

# Create the DynamoDB resource
dynamo = boto3.resource('dynamodb').Table(table_name)

# Define some functions to perform the CRUD operations
def update(payload):
    return dynamo.update_item(**{k: payload[k] for k in ['Key', 'UpdateExpression', 
    'ExpressionAttributeNames', 'ExpressionAttributeValues'] if k in payload})

operations = {'update': update}

def lambda_handler(event, context):
    operation = event['operation']
    payload = event['payload']
    
    if operation in operations:
        return operations[operation](payload)
        
    else:
        raise ValueError(f'Unrecognized operation "{operation}"')