import json
import uuid
import random

def generate_data(name, price):
    item_id = str(uuid.uuid4())
    item_data = {
        "item_id": item_id,
        "name": name,
        "price": price
    }
    return item_data

ITEMNAMES = ["Flannel Long Sleeve Shirt", "Ultra Light Down Jacket"]
ITEMPRICES = ["99.90", "39.90"]

items = []
for _ in range(5):
    idx = random.randint(0, len(ITEMNAMES) - 1)
    name = ITEMNAMES[idx]
    price = ITEMPRICES[idx]

    items.append(generate_data(name, price))

try:
    with open("data.json", "w") as file:
        json.dump(items, file, indent=2)
    print("Success")
except Exception as e:
    print(f"{e}")