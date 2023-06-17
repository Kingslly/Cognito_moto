from moto import mock_cognitoidp
import boto3
import pytest

@mock_cognitoidp
def test_signup():
    client = boto3.client('cognito-idp', region_name='us-west-2')
    
    # Create a user pool for testing
    user_pool = client.create_user_pool(PoolName='TestUserPool')
    user_pool_id = user_pool['UserPool']['Id']
    
    # Create a client app for the user pool
    client.create_user_pool_client(
        UserPoolId=user_pool_id,
        ClientName='TestClientApp'
    )
    
    # Perform signup request
    response = client.sign_up(
        ClientId='YOUR_CLIENT_ID',
        Username='testuser',
        Password='testpassword'
    )

    assert response['ResponseMetadata']['HTTPStatusCode'] == 200
    # Additional assertions or verifications