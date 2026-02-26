class Inventory():
    def __init__(self):
        self.items = {}

    def add_hundred_items(self, item):
        self.items[item] = 100

    def __iter__(self):
        return iter(self.items)
    
    def test_add(self, *args):
        for item in args:
            self.items[item] = 1


UQCA = Inventory()

UQCA.add_hundred_items("testing")

UQCA.test_add("testing1", "testing2", "testing3")

print(UQCA.items)

