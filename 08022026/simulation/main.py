import random
from datetime import datetime
import json

def random_itemcode():
    return random.randint(400000, 499999)

class Item:
    def __init__(self, name, itemcode, quantity):
        self.name = name
        self.itemcode = itemcode
        self.quantity = quantity

    def reduce_inv(self, amount=1):
        if self.quantity >= amount:
            self.quantity -= amount
            return True
        return False
    
    def restock(self, amount):  
        self.quantity += amount
        print(f"Restocked {self.name} by {amount}. New stock {self.quantity}")

class Employee:
    def stock_inv(self, item):
        restock_amount = random.randint(1, 15)
        item.restock(restock_amount)


class Customer:
    def purchase(self, item, amount=(random.randint(1, 101))):
        if item.reduce_inv(amount):
            print(f"Purchased {amount} unit(s) of {item.name}. Remaining stock: {item.quantity}")
        else:
            print("Not enough stock.")
            employee.stock_inv(item)



FleeceJacket = Item("Fleece Jacket", random_itemcode(), 100)
HEATTECH = Item("HEATTECH CREW NECK LONG SLEEVE T-SHIRT", random_itemcode(), 24)
CrewNeckTShirt = Item("CREW NECK T-SHIRT", random_itemcode(), 1489)

employee = Employee()
customer = Customer()
customer.purchase(FleeceJacket)
customer.purchase(HEATTECH)
customer.purchase(CrewNeckTShirt)