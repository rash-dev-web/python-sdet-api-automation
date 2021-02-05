import requests

URL = "https://reqres.in/api/users"
JSON_DATA = {
    "name": "morpheus",
    "job": "leader"
}

response = requests.post(url=URL, data=JSON_DATA)
print(response.json())  # response data

# status code
assert response.status_code == 201

# fetch id from response
print(response.json()["id"])
