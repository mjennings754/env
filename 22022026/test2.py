# build an inventory system
"""
create an inventory class, set the items to dictionary to be able to track the count within the class add a function to add items to it and change the count
"""
import random
class Inventory():
    def __init__(self):
        self.items = {}

    def add_item(self, item):
        if item in self.items:
            self.items[item] += 1
        else:
            self.items[item] = 1

    def consume_item(self, item):
        if item in self.items:
            if self.items[item] > 0:
                self.items[item] -= 1
            else:
                print(f"Cannot consume {item}, no stock left.")
        else:
            print(f"{item} not found in inventory")

    def generate_barcode(self):
        numbers = '0123456789'
        return ''.join(random.choices(numbers, k=24))

inv = Inventory()
inv.add_item("apple")
inv.add_item("eggs")
inv.add_item("eggs")
inv.consume_item("eggs") # should remove the count
inv.consume_item("eggs")
inv.consume_item("eggs")
inv.add_item("milk")
print(inv.generate_barcode())
print(inv.items)
