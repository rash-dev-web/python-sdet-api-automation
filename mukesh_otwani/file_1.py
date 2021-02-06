import requests

response = requests.get("https://reqres.in/api/users?page=2")
# print(response)  # <Response [200]>
# print(type(response))  # <class 'requests.models.Response'>
# print(dir(response))    # Display the content of an object:

# response status code
assert response.status_code == 200, "Response code doesn't match"
#
# # text / content / json()
# print(response.text)    # content of the response in unicode
# print(type(response.text))  # <class 'str'>
#
# print(response.content)  # content of the response in bytes
# print(type(response.content))   # <class 'bytes'>
#
# print(response.json())  # json encoded content of the response
# print(type(response.json()))    # <class 'dict'>

# headers / cookies / encoding / url
print(response.headers)
print(type(response.headers))   # <class 'requests.structures.CaseInsensitiveDict'>
print(response.cookies)
print(response.encoding)    # utf-8
print(response.url)  # https://reqres.in/api/users?page=2
