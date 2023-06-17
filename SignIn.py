import boto3

def signin(event, context):
    client = boto3.client('cognito-idp')
    
    username = event['username']
    password = event['password']
    
    response = client.initiate_auth(
        ClientId='YOUR_CLIENT_ID',
        AuthFlow='USER_PASSWORD_AUTH',
        AuthParameters={
            'USERNAME': username,
            'PASSWORD': password
        }
    )
    
    access_token = response['AuthenticationResult']['AccessToken']
    
    return {
        'statusCode': 200,
        'body': {
            'accessToken': access_token
        }
    }
