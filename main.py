import requests
import datetime
import os
from dotenv import load_dotenv
load_dotenv()

CLIENT_ID = os.environ['CLIENT_ID']
CLIENT_SECRET = os.environ['CLIENT_SECRET']
TENANT_ID = os.environ['TENANT_ID']

def get_access_token():
    url = f"https://login.microsoftonline.com/{TENANT_ID}/oauth2/v2.0/token"
    data = {
        'grant_type': 'client_credentials',
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'scope': 'https://graph.microsoft.com/.default'
    }
    response = requests.post(url, data=data)
    response.raise_for_status()
    return response.json().get('access_token')

def ping_graph_api():
    access_token = get_access_token()
    headers = {'Authorization': f'Bearer {access_token}'}
    res = requests.get('https://graph.microsoft.com/v1.0/users', headers=headers)
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{now}] PING Status: {res.status_code} - {res.reason}")

if __name__ == "__main__":
    ping_graph_api()
