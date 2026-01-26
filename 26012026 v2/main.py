# add data to json
import json
import random
import uuid

def generate_data(name, price):
    item_id = str(uuid.uuid4())
    item_data = {
        "item_id": item_id,
        "name": name,
        "price": price
    }
    return item_data

itemnames = ["Flannel Long Sleeve Shirt", "Slim Fit Chino Pants", "Fleece Full-Zip Jacket"]
itemprices = ["29.90", "39.90", "49.90"]

test_data = []

for _ in range(10):
    idx = random.randint(0, len(itemnames) - 1)
    name = itemnames[idx]
    price = itemprices[idx]
    test_data.append(generate_data(name, price))

with open("data.json", "w") as file:
    json.dump(test_data, file, indent=4)

print("Success")

# add a decorator

def changecase(func):
    def myinner():
        return func().upper()
    return myinner
@changecase
def myfunction():
    return "This should all be uppercase"

print(myfunction())