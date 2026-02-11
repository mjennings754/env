import json

data = ["test", 'testing', 'tester']

with open("data.json", "w") as f:
    json.dump(data, f, indent=3)


for _ in range(10):
    print(_)

x = lambda a : a + 10
print(x(5))

names = ["Spongebob", "Patrick", "Squidward"]
ages = [30, 25, 50]
jobs = ["Cook", "Unemployed", "Cashier"]

data = list(zip(names, ages, jobs))
print(data)