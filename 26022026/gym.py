"""
Exercise 1: Create a function in Python

Write a program to create a function that takes two arguments, name and age, and prints their values.
"""

def take_input(name, age):
    print(name, age)

take_input("Mitchell", "99")


"""
Exercise 2: Create a function with variable length of arguments
"""

def func1(*args):
    for arg in args:
        print(arg)

func1(20, 40, 60)