import requests

endpoint = "http://localhost:8000/api/products/2/update/"

data = {"title": "Baby bottle for small babies to drink milk or liquids"}

response_obj = requests.put(endpoint, json=data)

print(response_obj.status_code)
print(response_obj.json())
