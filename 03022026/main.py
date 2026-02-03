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

from dataclasses import dataclass
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

# Data class - a special kind of class that's designed mostly for holding data without
#              writing a lot of the boilerplater code for regular classes
#              they automatically generate: __init__, __repr__, __eq__
from dataclasses import dataclass, field
@dataclass (frozen=True) # frozen makes it immutable
class Person:
    name: str
    age: int
    password: str = field(repr=False)
    is_alive: bool = True

    def __post_init__(self):
        if self.age < 0:
            raise ValueError("Age cannot be negative")

person1 = Person("Spongebob", 40, "pineapple1")
person2 = Person("Patrick", 35, "password")


print(person1)
print(person2)
print(person1 == person2)

# zip combines multiple iterables

names = ["Spongebob", "Patrick", "Squidward"]
ages = [30, 25, 50]
jobs = ["Cook", "Unemployed", "Cashier"]

data = list(zip(names, ages, jobs))

print(data)
#<zip object at 0x102a82480>

for name, age, job in data:
    print(f"{name} is {age} years old {job}")

# recursion - a function that calls itself from within

#iterative
def walk(steps):
    for step in range(1, steps + 1):
        print(f"You take step #{step}")

walk(100)

#recursive (tends to be slower but easier to right)
def walk(steps):
        if steps == 0:
            return
        walk(steps - 1)
        print(f"You take step #{steps}")

walk(100)

#iterative

def factorial(x):
    result = 1
    if x > 0:
        for y in range(1, x + 1):
            result *= y
        return result
    
print(factorial(10))
    
#recursive
def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)
    
print(factorial(10))

import random

options = ("rock", "paper", "scissors")
running = True

while running:
    player = None
    computer = random.choice(options)
    while player not in options:
        player = input("Enter a choice (rock, paper, scissors): ")
    print(f"player: {player}")
    print(f"computer: {computer}")

    if player == computer:
        print("It's a tie!")
    elif player == "rock" and computer == "scissors":
        print("You win!")
    elif player == "paper" and computer == "rock":
        print("You win!")
    elif player == "scissors" and computer == "paper":
        print("You win!")
    else:
        print("You lose!")

    if not input("Play again? (y/n): ").lower() == "y":
        running = False

print("Thanks for playing!")