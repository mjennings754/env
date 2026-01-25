# generate test data in testdata.json

import uuid
from datetime import datetime
import json
import random
def generate_data(name, price):
    id = str(uuid.uuid4())

    data = {
        "id": id,
        "name": name,
        "price": price
    }

    return data

itemnames = ["ULTRA LIGHT DOWN JACKET", "FLANNEL L/S SHIRT", "SLIM FIT CHINO PANTS", "MERINO CREW NECK SWEATER", "CREW NECK LONG SLEEVE T-SHIRT"]
itemprices = ["99.90", "39.90", "59.90", "49.90", "29.90"]

test_data = []
for _ in range(100):
    idx = random.randint(0, len(itemnames) - 1)
    name = itemnames[idx]
    price = itemprices[idx]

    test_data.append(generate_data(name, price))

with open("testdata.json", "a") as file:
    json.dump(test_data, file, indent=4)
print("Success!")
