test = lambda x: x * 2
print(test(231232))
 

def add_airpods(func):
    def wrapper():
        print("* You purchase Airpods")
        func()
    return wrapper

def get_warranty(num):
    def decorator(func):
            def wrapper(*args, **kwargs):
                print(f"* You purchase {num} months warrenty")
                func(*args, **kwargs)
            return wrapper
    return decorator

@get_warranty(num=5)
@add_airpods
def get_iphone():
    print("* You get the iPhone 17 Pro")

get_iphone()