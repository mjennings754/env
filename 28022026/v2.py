# create a decorator
def special_offer(func):
    def wrapper():
        print("This item is on Special Offer for 39.90")
        func()
    return wrapper

@special_offer
def item():
    print("Fleece Full Zip Jacket")

item()

for i in range(1, 6):
    print(list[i])

import json
import uuid
import random

def generate_users(name):
    user_id = str(uuid.uuid4())
    user_data = {
        "user_id": user_id,
        "name": name
    }
    return user_data

USERNAMES = ["AzureSeal99214", "MonkeyPatch", "Farmer McGhee", "Zezima"]


users = []
for _ in range(5):
    idx = random.randint(0, len(USERNAMES) - 1)
    name = USERNAMES[idx]

    users.append(generate_users(name))

try:
    with open("users.json", "w") as file:
        json.dump(users, file, indent=2)
    print("Okay")
except Exception as e:
    print(e)