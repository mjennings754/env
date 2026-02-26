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

"""
Exercise 3: Return multiple values from a function
Write a function calculation() that accepts two variables and calculates both their addition and subtraction. 
The function should then return both the sum and the difference in a single return statement.
"""
def calculation(a, b):
    return(a + b, a - b)

res = calculation(40, 10)
print(res)