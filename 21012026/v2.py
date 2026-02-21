def print_even():
    for n in range(10):
        if n % 2 == 0:
            print(n)

print_even()

list1 = []
def even_to_list():
    for n in range(10):
        if n % 2 == 0:
            list1.append(n)
    return list1

print(even_to_list())


"""
Product Inventory Project - Create an application which manages an inventory of products. 
Create a product class which has a price, id, and quantity on hand. 
Then create an inventory class which keeps track of various products and can sum up the inventory value.
"""

class Product():
    def __init__(self, price, id, quantity):
        self.price = price
        self.id = id
        self.quantity = quantity

class Inventory():
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def total(self):
        total = 0
        for product in self.products:
            total += product.value()
        return total
"""
def print_odd():
    x = int(input("Enter a number: "))
    for i in range(x):
        if i % 2 != 0:
            print(i)
    
print_odd()
"""


list2 = []
for i in range(10):
    list2.append(i)

import random
letters = "abcdef"
numbers = "1234567890"

hex = letters + numbers

length = 6
hex_value = ''.join(random.choice(hex) for _ in range(length))

print(f"#{hex_value}")


items = {key: key*key for key in range(10)}
print(items)

double = lambda x: x * 2
print(double(2))

triple = lambda x: x * 3
print(triple(9))

num_list = []
for i in range(5):
    num_list.append(i)

print(num_list)

dict_a = {'a': 10, 'b': 20}
dict_b = {'a': 20, 'b': 30}

def merge_dict(dict1, dict2):
    res = dict1.copy()
    for key, value in dict2.items():
        res[key] = res.get(key, 0) + value
    return res

merged = merge_dict(dict_a, dict_b)
print(merged)

words = ["apple", "bat", "cherry", "dog", "elderberry"]

newlist2 = [word.upper() for word in words if len(word) >= 4]
print(newlist2)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = next

    def reverse(self):
        prev, curr = None, curr.next
        while curr:
            next_node = curr.next
            curr.next = prev
            prev, curr = curr, next_node
        self.head = prev


