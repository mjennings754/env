# create a decorator


def special_offer(func):
    def wrapper():
        print("This item is on Special Offer for 39.90")
        func()
    return wrapper

@special_offer
def item():
    print("Fleece Full Zip Jacket")

item()