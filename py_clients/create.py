import requests

endpoint = "http://localhost:8000/api/products/"
data = {
    "title": "Baby Toy keys",
    "price": 1.55,
    "title": "keys for the babies to chew"
}
response_obj = requests.post(endpoint, json=data)

print(response_obj.status_code)
print(response_obj.json())
