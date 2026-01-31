import json
import csv

def generate_data(name):
    item_data = {
        "name": name
    }
    return item_data

data = ["Heattech Ultra Warm Crew Neck Long Sleeve", "Airism V Neck T-Shirt", "Ultra Light Down Jacket"]
test_data = []
for _ in range(10):
    name = data

    test_data.append(generate_data(name))
with open("test.json", "w") as file:
    json.dump(test_data, file, indent=1)
print("Success")