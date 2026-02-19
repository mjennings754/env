import json

def generate_data(name):
    item_data = {
        "name": name
    }
    return item_data

itemnames = ["TESTING"]

testdata = []

for _ in range(1):
    name = itemnames
    testdata.append(generate_data(name))

with open("data.json", "w") as file:
    json.dump(testdata, file, indent=1)

print("Successful")