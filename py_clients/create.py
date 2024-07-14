import requests

endpoint = "http://localhost:8000/api/products/"
data = {
    "title": "Baby Showrma",
    "price": 7.55,
    "title": "Baby Showrma for baby to play around"
}
response_obj = requests.post(endpoint, json=data)

print(response_obj.status_code)
print(response_obj.json())
