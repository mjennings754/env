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

    # model a purchase

    def purchase(self, item):
        if item in self.items:
            if self.items[item] > 0:
                self.items[item] -= 1
            else:
                print("error")

UQJP = Inventory()
UQJP.add_item("フリース フルジップ ジャケット")
UQJP.add_item("フリース フルジップ ジャケット")
UQJP.add_item("スリムフィットチノパンツ")
UQJP.purchase("フリース フルジップ ジャケット")
UQJP.purchase("フリース フルジップ ジャケット")
UQJP.purchase("フリース フルジップ ジャケット")
print(UQJP.items)