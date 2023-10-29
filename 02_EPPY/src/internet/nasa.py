import requests

api_key = 'G2bDv9U4jmyC9YhrWj6E0QK6vyMU8ww6Gg6NuI5a'
base_url = 'https://api.nasa.gov/mars-photos/api/v1/'
end_point = 'rovers/curiosity/photos'
params = {'earth_date': '2015-6-3', 'api_key' : api_key}

response = requests.get(base_url + end_point, params = params)

if response:
    print(response.json()['photos'][0])
else:
    raise Exception(f"Error {response.status_code}")

response_img = requests.get(response.json()['photos'][0]['img_src'])

if response_img:
    with open('mars.jpg', 'wb') as file:
        file.write(response_img.content)