import requests

UUID = '64234f58-7e20-43bb-a802-50f09c08bfec'
url = "http://54.85.100.225:8000"

def moveWarrior(direction):
    r = requests.post(url + "/api/game", json={'account_uuid': UUID, "action": "move",
                                               "direction": direction})
    if r.status_code != "200":
        print ("Error: %s Text: %s",r.status_code)
    print(r.text)
    return r.text

def restartGame():
    r = requests.post(url + "/api/game", json={'account_uuid': UUID,
                                               "action": "restart"})
    print(r.text)
    return r


restartGame()
moveWarrior("north")
moveWarrior("north")
