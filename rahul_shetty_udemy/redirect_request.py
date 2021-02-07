import requests

response = requests.get("http://github.com/")
print(response.url)  # https://github.com/
print(response.status_code)  # 200
print(response.history)  # [<Response [301]>]

# disable redirect
response = requests.get("http://github.com/", allow_redirects=False)
print(response.status_code)  # 301
print(response.history)  # []

# enable redirect
response = requests.head("http://github.com/", allow_redirects=True)
print(response.status_code)  # 200
print(response.history)  # [<Response [301]>]

