"""
Exercise 1: Create a function in Python

Write a program to create a function that takes two arguments, name and age, and prints their values.
"""

def display(name, age):
    print(name, age)

display("test", 99)

"""
Exercise 2: Create a function with variable length of arguments

Write a program to create a function func1() that accepts a variable number of arguments and prints each of their values.
"""

def func1(*args):
    for arg in args:
        print(arg)

func1(20, 30, 40)