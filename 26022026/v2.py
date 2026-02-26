class Inventory():
    def __init__(self):
        self.items = {}

    def add_hundred_items(self, item):
        self.items[item] = 100

    def __iter__(self):
        return iter(self.items)

UQCA = Inventory()

UQCA.add_hundred_items("testing")

for items in UQCA:
    print(items)