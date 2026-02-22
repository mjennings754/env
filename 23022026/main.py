# create an inventory system

class Inventory():
    def __init__(self):
        self.items = {}

    def add_item(self, item):
        self.items[item] = 1
        
UQJP = Inventory()
UQJP.add_item("フリース フルジップ ジャケット")
UQJP.add_item("フリース フルジップ ジャケット")
print(UQJP.items)