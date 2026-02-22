# build an inventory system

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
inv.add_item("apple")
inv.add_item("milk")
print(inv.items)