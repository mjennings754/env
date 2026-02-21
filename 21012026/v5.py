my_list = [i for i in range(1,10)]
print(my_list)

my_dict = {i: i**2 for i in range(1, 10)}
print(my_dict)

class monkey:
    def patch(self):
        print("patch() is being called")

def monk_p(self):
    print("monk_p() is being called")

monkey.patch = monk_p

obj = monkey()

obj.patch()


def uppercase(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    
    return wrapper

def say_hi():
    return 'hello there'

decorate = uppercase(say_hi)
print(decorate())


try:
    f = open('test.txt', 'r')
except FileNotFoundError:
    print("File not found")

def goosebumps():
    pass

goosebumps()