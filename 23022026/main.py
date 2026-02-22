# create an inventory system

class Inventory():
    def __init__(self):
        self.items = {}
    # what if the item already exists?
    def add_item(self, item):
        if item in self.items:
            self.items[item] += 1
        else:
            self.items[item] = 1

UQJP = Inventory()
UQJP.add_item("フリース フルジップ ジャケット")
UQJP.add_item("フリース フルジップ ジャケット")
UQJP.add_item("スリムフィットチノパンツ")
print(UQJP.items)