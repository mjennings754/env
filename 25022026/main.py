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