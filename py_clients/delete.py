import requests

endpoint = "http://localhost:8000/api/products/"
response_obj = requests.get(endpoint)

available_obj_list = [obj.get("id") for obj in response_obj.json()]

print(f"Available objects : {available_obj_list}")
id_to_delete = input("Which object of above you want to delete : ")


endpoint = f"http://localhost:8000/api/products/{id_to_delete}/delete"

response_obj = requests.delete(endpoint)
9
print(response_obj.status_code)
