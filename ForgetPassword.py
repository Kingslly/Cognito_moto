import boto3

def forgot_password(event, context):
    client = boto3.client('cognito-idp')
    
    username = event['username']
    
    response = client.forgot_password(
        ClientId='YOUR_CLIENT_ID',
        Username=username
    )
    
    return {
        'statusCode': 200,
        'body': 'Password reset initiated successfully.'
    }
