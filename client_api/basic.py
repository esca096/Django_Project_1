import requests

endpoint = "http://127.0.0.1:8080/api/"
reponse = requests.post(endpoint, json={'name':'ananas', 'content':'just ananas', 'price':45})
print(reponse.json())
print(reponse.status_code)

#HTTP REQUEST --> HTML
#REST API HTTP --> JSON
