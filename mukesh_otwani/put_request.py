import requests

payload_data = {
    "name": "morpheus",
    "job": "zion resident"
}

response = requests.put("https://reqres.in/api/users/2", data=payload_data)
print(response.json())

assert response.json()["name"] == "morpheus"
assert response.status_code == 200

