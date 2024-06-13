import requests
id = input("enter the id that you want to show : ")
endpoint = f"http://127.0.0.1:8080/apps/{id}/details"
reponse = requests.get(endpoint)
print(reponse.json())
print(reponse.status_code)
