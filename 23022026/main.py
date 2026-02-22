# create an inventory system
import random
import json
import os
class Inventory():
    def __init__(self, filename="inventory.json"):
        self.items = {}
        self.filename = filename
        self.load()
    # what if the item already exists?
    def add_item(self, item):
        if item in self.items:
            self.items[item] += 1
        else:
            self.items[item] = 1
        self.save()

    def save(self):
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(self.items, f, ensure_ascii=False, indent=4)

    def load(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                self.items = json.load(f)
        else:
            self.items = {}

    # model a purchase

    def purchase(self, item):
        if item in self.items:
            if self.items[item] > 0:
                self.items[item] -= 1
                self.save()
            else:
                print("error")

    # how to simulate a delivery

    def delivery(self):
        itemnames = ["フリース フルジップ ジャケット", "スリムフィットチノパンツ", "フランネルシャツ", "ブロードクロスシャツ", "ワイドフィットジーンズ"]
        quantity = random.randint(1, 200)
        random_item = random.choice(itemnames)
        print(f"配達\n{random_item}: {quantity}")
        if random_item in self.items:
            self.items[random_item] += quantity
        else:
            self.items[random_item] = quantity
        self.save()

    

UQJP = Inventory()
UQJP.add_item("フリース フルジップ ジャケット")
UQJP.add_item("フリース フルジップ ジャケット")
UQJP.add_item("スリムフィットチノパンツ")
UQJP.purchase("フリース フルジップ ジャケット")
UQJP.purchase("フリース フルジップ ジャケット")
UQJP.delivery()
print(UQJP.items)