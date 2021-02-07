import requests

URL = "https://httpbin.org/cookies"
user_cookie = {
    "user": "Mir",
}

se = requests.session()

response = se.get(URL, cookies=user_cookie)
print(response.json())  # {'cookies': {'user': 'Mir'}}
se.cookies.update({"user": "Ayaan"})
response = se.get(URL)
print(response.json())  # {'cookies': {'user': 'Ayaan'}}

