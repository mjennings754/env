test = lambda x: x * 2
print(test(231232))
 

def purchase_game(func):
    def wrapper():
        print("* You purchased Borderlands 4")
        func()
    return wrapper

def game_library(games):
    def decorator(func):
        def wrapper():
            print(f" * You have {games} games in your Steam Library")
            func()
        return wrapper
    return decorator
@game_library(games="202")
@purchase_game
def create_steam_account():
    print("You created a Steam account")

create_steam_account()
