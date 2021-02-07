import requests
from rahul_shetty_udemy.configuration import get_config
from rahul_shetty_udemy.resources import Resources

# read data from .ini file

# get request
get_param = {
    "page": 2,
}

url = get_config()["API"]["endpoint"] + Resources.get_user

response = requests.get(url, params=get_param)
assert response.status_code == 200

# post request
post_data = {
    "name": "morpheus",
    "job": "leader"
}
response = requests.post("https://reqres.in/api/users", data=post_data)
assert response.status_code == 201

# put request
put_payload = {
    "name": "morpheus",
    "job": "zion resident"
}
response = requests.put("https://reqres.in/api/users/2", data=put_payload)
assert response.status_code == 200

# patch request
patch_payload = {
    "name": "morpheus",
}
response = requests.patch("https://reqres.in/api/users/2", data=patch_payload)
assert response.status_code == 200

# delete request
response = requests.delete("https://reqres.in/api/users/2")
assert response.status_code == 204
