# append to a list using a for loop
list1 = []
for i in range(10):
    list1.append(i)
print(list1)

# print the middle of the list
middle = len(list1) // 2
print(middle)

# reverse the list
print(list1[::-1])

# create a for loop that keeps track of the previous element

for i in range(10):
    prev = i-1
    print(i, prev)

# create a decorator

def purchase_airpods(func):
    def wrapper():
        print("* You purchase AirPods")
        func()
    return wrapper

@purchase_airpods
def purchase_iphone():
    print("You purchase an iPhone 17 Pro")

purchase_iphone()

# with the decorator mentioned above create another function and takes an argument

def get_warranty(num):
    def decorator(func):
        def wrapper():
            print(f"You get {num} months warranty")
            func()
        return wrapper
    return decorator


def purchase_airpods(func):
    def wrapper():
        print("* You purchase AirPods")
        func()
    return wrapper

@get_warranty(num=12)
def purchase_iphone():
    print("You purchase an iPhone 17 Pro")

purchase_iphone()