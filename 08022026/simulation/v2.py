import random

def random_itemcode():
    return random.randint(400000, 499999)

class Inventory:
    def __init__(self, name, itemcode, quantity):
        self.name = name
        self.itemcode = itemcode
        self.quantity = quantity

    def receive(self, amount=1):
        amount = random.randint(1, 124)
        self.quantity += amount
        print(f"You have received {amount} units in Delivery")

item1 = Inventory("test", random_itemcode(), 23)
print(item1.receive())