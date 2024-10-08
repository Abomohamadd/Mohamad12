import google_auth_oauthlib.flow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
import requests

# Set up the OAuth2 flow
flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
    'client_secret.json',
    scopes=['https://www.googleapis.com/auth/youtube.force-ssl']
)

authorization_url, state = flow.authorization_url(
    access_type='offline',
    include_granted_scopes='true'
)

# Redirect the user to the authorization URL to login and authorize the app
print('Please go to this URL and authenticate:', authorization_url)
authorization_response = input('Enter the full callback URL: ')

# Exchange the authorization response for credentials
flow.fetch_token(authorization_response=authorization_response)

# Get the credentials
credentials = flow.credentials

# Use the credentials to make API requests
api_url = "https://www.googleapis.com/youtube/v3/subscriptions?part=snippet"
subscription_data = {
    "snippet": {
        "resourceId": {
            "channelId": "UC9m1E1BvZQDYSyADFkEHPgg"
        }
    }
}

headers = {
    "Authorization": f"Bearer {credentials.token}",
    "Content-Type": "application/json"
}

response = requests.post(api_url, json=subscription_data, headers=headers)

if response.status_code == 200:
    print("Subscription successful!")
else:
    print("Subscription failed. Error:", response.text)