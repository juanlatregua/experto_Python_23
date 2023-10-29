import requests

client_id = '02878d59fb1341f3fd05'
client_secret = 'c6b804965e0851ea8ab6a428443c52eecfe0ac2a'
redirect_uri = 'https://httpbin.org/anything'

base_url = 'https://github.com/'

def create_oauth_link():
    endpoint = "/login/oauth/authorize"

    params = {
        "client_id" : client_id,
        "redirect_uri" : redirect_uri,
        "scope" : 'user'
    }

    response = requests.get(base_url + endpoint, params = params)

    return response

def exchange_code_for_token(code):
    endpoint = '/login/oauth/access_token'

    params = {
        "client_id" : client_id,
        "client_secret" : client_secret,
        "redirect_uri" : redirect_uri,
        "code" : code
    }

    headers = {"Accept": "application/json"}

    response = requests.get(base_url + endpoint, params = params, headers = headers)

    if response:
        return response.json()['access_token']
    else:
        raise Exception("Impossible to get Token")


def user_info(token):
    base_url = 'https://api.github.com/'
    endpoint = 'user'

    headers = {"Authorization" : f"token {token}"}

    response = requests.get(base_url + endpoint, headers = headers).json()

    return f"name = {response['name']}, email = {response['email']}, total_private_repos = {response['total_private_repos']}"


# resp = create_oauth_link()
# print(resp.url)

# code = input("Github Code please... ")
# token = exchange_code_for_token(code)

# print(f"code = {code}, Token = {token}")

token = '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'
print(user_info(token))
