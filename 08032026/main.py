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

"""
Exercise 3: Return multiple values from a function

Write a function calculation() that accepts two variables and calculates both their addition and subtraction. The function should then return both the sum and the difference in a single return statement.
"""
def calculation(a, b):
    addition = a + b
    subtraction = a - b
    return(addition, subtraction)

res = calculation(40, 10)
print(res)

"""
Exercise 4: Create a function with a default argument

Write a program to create a function show_employee() with the following specifications:

It should accept the employee’s name and salary.
It should display both the name and salary.
If the salary is not provided in the function call, it should default to 9000.
"""
def show_employee(name, salary=9000):
    return(f"name: {name}, salary: {salary}")

print(show_employee("Ben", 12000))
print(show_employee("Jessa"))

"""
Exercise 5: Create an inner function

Create a program with nested functions to perform an addition calculation as follows:

Define an outer function that accepts two parameters, a and b.
Inside this outer function, define an inner function that calculates the sum of a and b.
The outer function should then add 5 to this sum.
Finally, the outer function should return the resulting value.”
"""
def outer(a, b):
    def inner(a, b):
        return a + b
    
    add = inner(a, b)

    return add + 5

res = outer(5, 10)
print(res)
    