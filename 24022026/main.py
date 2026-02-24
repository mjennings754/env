# create a decorator

def decorator(func):
    def wrapper():
        print("Hello")
        func()
    return wrapper


@decorator
def purchase_iphone():
    print("You have purchased an iphone")

purchase_iphone()