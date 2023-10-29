import requests

api_key = '1II8NzpUh9f1gu3PNDQvWPhie5BGdL1o'
base_url = 'https://api.giphy.com/v1/gifs/'
endpoint = 'trending'

params = {
    'api_key': api_key,
    'limit': 5
}

response = requests.get(base_url+endpoint, params=params)

if not response:
    raise Exception(response.status_code)

for gif in response.json()['data']:
    print(f"Title = {gif['title']}, URL = {gif['url']}")

print("")

endpoint = 'search'
params['q'] = "rick morty"

response = requests.get(base_url+endpoint, params=params)

if not response:
    raise Exception(response.status_code)

for gif in response.json()['data']:
    print(f"Title = {gif['title']}, URL = {gif['url']}")
    title = gif['title']
    url = gif['images']['original']['mp4']

    with open(f"{title}.mp4", 'wb') as file:
        file.write(requests.get(url).content)