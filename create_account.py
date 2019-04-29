import requests

url = "http://54.85.100.225:8000"
r = requests.post(url+"/api/account" , json={"name":"Team Warrior"})
print(r)
print(r.status_code)
print(r.json())
