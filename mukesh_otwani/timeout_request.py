import requests

# request will fail if no response in 10 seconds
response = requests.get("https://httpbin.org/delay/5", timeout=10)
assert response.status_code == 200
