import requests

endpoint = "http://127.0.0.1:8080/apps/12/update"
reponse = requests.put(endpoint, json={'name':'Naruto', 'content':'Uzumaki', 'price':500})
print(reponse.json())
print(reponse.status_code)