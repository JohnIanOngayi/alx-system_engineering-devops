#!/usr/bin/python3
import requests
from requests.auth import HTTPBasicAuth
from os import getenv

CLIENT_ID = getenv('client_id')
SECRET_KEY = getenv('secretKey')
password = getenv('passWord')
redditUser = getenv('redditUser')

auth = HTTPBasicAuth(CLIENT_ID, SECRET_KEY)

data = {
    'grant_type': 'password',
    'username': redditUser,
    'password': password
}

headers = {'User-Agent': 'My User Agent 1.0'}

res = requests.post('https://www.reddit.com/api/v1/access_token',
                    auth=auth, data=data, headers=headers)

token = res.json()['access_token']
print(token)

headers['Authorization'] = f'bearer {token}'

res_auth = requests.get('https://oauth.reddit.com/api/v1/me', headers=headers)
print(res_auth.status_code)
