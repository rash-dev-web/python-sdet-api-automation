import requests
import json

with open("data.json") as data_file:
    payload = data_file.read()

response = requests.post("https://reqres.in/api/users", data=json.loads(payload))

# validate header content type
headers_values = response.headers
assert "application/json" in headers_values["Content-Type"]
