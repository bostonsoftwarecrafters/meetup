import requests

url = "http://54.85.100.225:8000"
r = requests.post(url+"/api/account" , json={"name":"Ethan"})
print("Text")
print(r.text)
print("Status")
print(r.status_code)
print("JSON")
print(r.json())
