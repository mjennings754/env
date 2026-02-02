double = lambda x : x * 2
print(double(5))

add = lambda x, y: x + y
print(add(4, 5))

# Map() Applies a given given function to all items in a collections

def c_to_f(temp):
    return (temp * 9/5) + 32

celsius_temps = [0.0, 10.0, 45.0, 43.0, 50.0, 44.0]
# typecase the map the a list
fahrenheit_temps = list(map(c_to_f, celsius_temps))

print(fahrenheit_temps)
#<map object at 0x1049c28c0>

for temp in fahrenheit_temps:
    print(temp)

# lambda usage

f_temps = list(map(lambda temps: (temp * 9/5) + 32,celsius_temps))

print(f_temps)

# filter(function, collection) - return all elements that pass a condition

def is_passing(grade):
    return grade >= 60

grades = [91, 43, 43, 65, 7, 68]

passing_grades = filter(is_passing, grades)

print(passing_grades)
#<filter object at 0x1026a75e0>

for grade in passing_grades:
    print(grade)

# reduce(function, collection) - reduces elements in a collection to a single value

from functools import reduce

def add(x, y):
    return x + y

prices = [19.99, 1.00, 5.00, 5.45]

total = reduce(add, prices)

print(f"${total}")

total_two = reduce(lambda x, y: x + y, prices)

print(f"${total_two}")

# decorator a function that extends the behavior of another function

def add_sprinkles(func):
    def wrapper(*args, **kwargs):
        print("*You add sprinkes")
        func(*args, **kwargs)
    return wrapper

def add_fudge(func):
    def wrapper(*args, **kwargs):
        print("* You add fudge ")
        func(*args, **kwargs)
    return wrapper

@add_sprinkles
@add_fudge
def get_ice_cream(flavor):
    print(f"Here is your {flavor} ice cream [ ]")

get_ice_cream("vanilla")