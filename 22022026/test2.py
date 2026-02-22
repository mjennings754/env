# build an inventory system
"""
create an inventory class, set the items to dictionary to be able to track the count within the class add a function to add items to it and change the count
"""
class Inventory():
    def __init__(self):
        self.items = {}

    def add_item(self, item):
        if item in self.items:
            self.items[item] += 1
        else:
            self.items[item] = 1

inv = Inventory()
inv.add_item("apple")
inv.add_item("eggs")
inv.add_item("milk")
print(inv.items)