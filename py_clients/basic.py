import requests

endpoint = "http://localhost:8000/api/"

# response_obj = requests.get(
#     endpoint,
#     params={"user": "itachi"},
#     json={"query": "Hello world", 'message': 'Hello this is your Django API response'})
response_obj = requests.post(
    endpoint,
    params={"user": "itachi"},
    json={"title": "Baby bottle"})

print(response_obj.status_code)
print(response_obj.json())
