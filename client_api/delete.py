import requests
id = input("enter the id that you want to delete : ")
endpoint = f"http://127.0.0.1:8080/apps/{id}/delete"
reponse = requests.delete(endpoint)
print(reponse.status_code, reponse.status_code==204)