import requests

endpoint = "http://localhost:8000/api/products/2/"

response_obj = requests.get(
    endpoint,
    params={"user": "itachi"},
    json={"title": "Baby bottle"})

print(response_obj.status_code)
print(response_obj.json())
