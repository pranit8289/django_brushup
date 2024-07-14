import requests

endpoint = "https://httpbin.org/anything"

response_obj = requests.get(endpoint, json={"query": "Hello world"})

print(response_obj.json())