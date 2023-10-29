import requests

url_base = "https://randomuser.me"
end_point = '/api/'
q_params = {"gender": "female", "nat" : "es"}

response = requests.get(url_base + end_point, params = q_params
)

print(response.status_code)

if response:
    print(response.json())
else:
    print('An error has occurred.')
