import requests
from getpass import getpass
#concerne la method list
"""endpoint = 'http://127.0.0.1:8080/apps/auth'
username = input("Entrez votre username : ")
password = getpass("entrez votre mot de passe : ")
auth_response = requests.post(endpoint, json={'username':username, 'password':password})
print(auth_response.json())
print(auth_response.status_code)



if auth_response.status_code == 200:"""  
endpoint = "http://127.0.0.1:8080/apps/create/"
headers = {
        'Authorization':'Bearer 2b3beda13f305c4709b0f7e997568c38efad1d6b'
    }
reponse = requests.get(endpoint, headers=headers)
print(reponse.json())
print(reponse.status_code)