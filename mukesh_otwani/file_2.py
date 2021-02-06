import requests

response = requests.get("https://reqres.in/api/users?page=2")
json_response = response.json()
print(json_response["total_pages"])
assert json_response["total_pages"] == 2, "total page count is not matching"

print(json_response["total"])
assert json_response["total"] == 12, "total count is not matching"

print(json_response["data"][0]["email"])    # michael.lawson@reqres.in
assert (json_response["data"][0]["email"]).endswith("reqres.in"), "Email format is not matching"

assert (json_response["data"][4]["last_name"]) is not None


# using params
parameter = {
    "page": 2
}
response = requests.get("https://reqres.in/api/users", params=parameter)



