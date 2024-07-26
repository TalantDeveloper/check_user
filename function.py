import requests
from requests.auth import HTTPBasicAuth


def chech_endpoint(api, port, username, password):
    ARI_URL = f'http://{api}:{port}/ari/endpoints'
    response = requests.get(ARI_URL, auth=HTTPBasicAuth(username, password))
    if response.status_code == 200:
        # Parse the JSON response2003
        channels_data = response.json()
        for channel in channels_data:
            if channel['state'] == 'online':
                print(f"{channel['resource']} online")
            else:
                print(f"{channel['resource']} offline")
    else:
        print(f"Failed to get channels data. Status code: {response.status_code}, Response: {response.text}")


def check_channels(api, port, username, password):
    ARI_URL = f'http://{api}:{port}/ari/channels'
    response = requests.get(ARI_URL, auth=HTTPBasicAuth(username, password))
    if response.status_code == 200:
        channels_data = response.json()
        for channel in channels_data:
            print(f"channel-> {channel}")
    else:
        print(f"Failed to get channels data. Status code: {response.status_code}, Response: {response.text}")

