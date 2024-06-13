import requests

endpoint = "http://127.0.0.1:8080/apps/create/"
reponse = requests.post(endpoint, json={'name':'Demon', 'content':'Slayer', 'price':450})
print(reponse.json())
print(reponse.status_code)