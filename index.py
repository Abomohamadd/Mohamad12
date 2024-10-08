import requests

api_url = "https://www.googleapis.com/youtube/v3/subscriptions?part=snippet"
api_key = "AIzaSyALpocbn4k-NcEaQCge7WNkxaKfy-coSj0"

subscription_data = {
    "snippet": {
        "resourceId": {
            "channelId": "UC9m1E1BvZQDYSyADFkEHPgg"
        }
    }
}

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

response = requests.post(api_url, json=subscription_data, headers=headers)

if response.status_code == 200:
    print("Subscription successful!")
else:
    print("Subscription failed. Error:", response.text)