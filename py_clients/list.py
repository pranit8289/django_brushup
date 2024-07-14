import requests

endpoint = "http://localhost:8000/api/products/"
response_obj = requests.get(endpoint)

print(response_obj.status_code)
print(response_obj.json())
