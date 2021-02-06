import requests

payload = {
    "name": "mir",
    "job": "tester"
}

response = requests.post("https://reqres.in/api/users", data=payload)
print(response)  # <Response [201]>
print(response.json())  # response json
assert response.json()["name"] == "mir"
