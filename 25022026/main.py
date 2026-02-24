# create a decorator that takes an input

def purchase_membership(months):
    def decorator(func):
        def wrapper():
            print(f"You have purchased {months} membership")
            func()
        return wrapper
    return decorator


@purchase_membership(months="12")
def create_osrs_account():
    print("You have created an OSRS account!")

create_osrs_account()

# create an inventory system

class Inventory():
    def __init__(self):
        self.items = {}

    def add_items(self, item):
        self.items[item] = 1

UQ = Inventory()
print(UQ)
UQ.add_items("Chino Pants")
print(UQ.items)

# create a for loop that shows the prev number

for i in range(10):
    prev = i-1
    print(i, prev)
