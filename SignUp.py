import boto3


def signup(event, context):
    client = boto3.client('cognito-idp')
    
    username = event['username']
    password = event['password']
    
    response = client.sign_up(
        ClientId='YOUR_CLIENT_ID',
        Username=username,
        Password=password
    )
    
    return {
        'statusCode': 200,
        'body': 'User signed up successfully.'
    }
