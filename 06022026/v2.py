import json
initial_contact = input("Do you want to input more protein intake? (y/n)")
protein = []
if initial_contact == 'y':
    protein_intake = int(input("How much protein is in the meal? "))
    protein.append(protein_intake)
    with open('data.json', 'w') as f:
        json.dump(protein, f)
else:
    with open('data.json', 'r') as f:
        loaded_data = json.load(f)
    print(loaded_data)