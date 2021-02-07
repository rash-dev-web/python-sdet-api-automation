import requests

url = 'https://httpbin.org/post'

files = {
    "file": open("sample.txt", "rb")
}
response = requests.post(url, files=files)
response.raise_for_status()
print(response.text)
print(response.status_code)
