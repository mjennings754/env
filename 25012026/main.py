# Generate test json data
import json
from datetime import datetime
import uuid

def generate_data(name):
    id = str(uuid.uuid4())
    data = {
        "timestamp": datetime.now().isoformat(),
        "name": name
    }
    return data

dataname = ["testName"]
test_data = []
for i in range(5):
    name = dataname

    test_data.append(generate_data(name))

try:
    with open("data.json", "w") as file:
        json.dump(test_data, file, indent=2)
    print("Success")
except Exception as e:
    print(f"{e}")