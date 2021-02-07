import requests

response = requests.get("https://github.com/", timeout=0.001)
# requests.exceptions.ConnectTimeout: HTTPSConnectionPool(host='github.com', port=443): Max retries exceeded with url: / (Caused by ConnectTimeoutError(<urllib3.connection.HTTPSConnection object at 0x0416A268>, 'Connection to github.com timed out. (connect timeout=0.001)'))