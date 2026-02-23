# create an inventory system

class Inventory():
    def __init__(self):
        self.items = {}

    def add_items(self, item):
        self.items[item] = 1


test = Inventory()
print(test)
test.add_items("test")
print(test.items)

# create lambda

testing = lambda x: x * 2

print(testing(2))