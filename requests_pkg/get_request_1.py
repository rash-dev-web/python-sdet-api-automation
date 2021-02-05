import requests
import json

get_paramaters = {
    "page": 2
}
response = requests.get("https://reqres.in/api/users?page=2", params=get_paramaters)
# print(response.text)  # whole response
# print(type(response.text))  # <class 'str'>
# print(json.loads(response.text))
# print(type(json.loads(response.text)))  # <class 'dict'>
# # or
# print(type(response.json()))  # <class 'dict'>
# # print a value from json response
json_response = response.json()
# print(json_response["data"][0]["first_name"])  # Michael

# verify status code
assert response.status_code == 200

# print the headers
request_headers = response.headers
print(request_headers)  # all the headers in dict
print(type(request_headers))    # <class 'requests.structures.CaseInsensitiveDict'>
print(request_headers["Date"])  # Fri, 05 Feb 2021 17:05:14 GMT

# cookies
print(response.cookies)
