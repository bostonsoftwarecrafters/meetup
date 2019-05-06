import requests
import random

UUID = '510b50eb-1ec4-474a-a8e4-982ed1963566'
url = "http://54.85.100.225:8000"

def moveWarrior(direction):
    r = requests.post(url + "/api/game", json={'account_uuid': UUID, "action": "move",
                                               "direction": direction})
    if r.status_code != 200:
        print ("Error: %s Text: %s",r.status_code)
    return r

def restartGame():
    r = requests.post(url + "/api/game", json={'account_uuid': UUID,
                                               "action": "restart"})
    return r

def getrandomdir():
    print("********** moving in random direction")
    dirInt = random.randint(1,4)
    if dirInt == 1:
        return "north"
    elif dirInt == 2:
        return "south"
    elif dirInt == 3:
        return "east"
    else:
        return "west"



r =  restartGame()

inventory = r.json()["inventory"]

print("inventory: ")
print(inventory)

labrinth = [] * 10
for i in range(10):
   labrinth.append([] * 10)

print(labrinth)

nearby = dict()
dir = 'north'
for x in range(11):
    result = moveWarrior(dir).json()
    print(result["inventory"])
    if result["game"] == "Over":
        break

    nearhere = result["nearby"]
    nearby[result["location"]] = nearhere

    if "Pit" in nearhere:
        dir = getrandomdir()
    elif "Rope" in nearhere or "Magic Arrow" in nearhere:
        result = moveWarrior("north").json()
        result = moveWarrior("south").json()
        result = moveWarrior("east").json()
        result = moveWarrior("west").json()
        result = moveWarrior("west").json()
        result = moveWarrior("east").json()
        result = moveWarrior("south").json()
        result = moveWarrior("north").json()

    print(nearby)

