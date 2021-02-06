import requests

request_payload = {
    "name": "morpheus",
}

response = requests.patch("https://reqres.in/api/users/2", data=request_payload)
print(response.json())

assert response.json()["name"] == "morpheus"
assert response.status_code == 200
