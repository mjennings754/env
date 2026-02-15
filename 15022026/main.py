list1 = [1, 2, 3, "hello", "testing", 49.0]
newlist = [item for item in list1 if isinstance(item, (int))]

print(newlist)

nested = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
number_5 = nested[1][1]
print(number_5)

# check if a number in palindrome

def is_palindrome(n):
    original = str(n)
    reversed = original[::-1]

    if original == reversed:
        print("True")
    else:
        print("False")

is_palindrome(989)


"""
Exercise 1: Create a function in Python

Write a program to create a function that takes two arguments, name and age, and prints their values.
"""
def take_input(name, age):
    print(name, age)

take_input("William", 190)


"""
Exercise 2: Create a function with variable length of arguments

Write a program to create a function func1() that accepts a variable number of arguments and prints each of their values.
"""

def func1(*args):
    for arg in args:
        print(arg)

func1(10, 20, 20)
func1(10, 20)

"""
Exercise 3: Return multiple values from a function

Write a function calculation() that accepts two variables and calculates both their addition and subtraction. The function should then return both the sum and the difference in a single return statement.
"""

def calculation(a, b):
    addition = a + b
    subtraction = a - b

    return addition, subtraction

res = calculation(20, 10)
print(res)


"""
Exercise 4: Create a function with a default argument

Write a program to create a function show_employee() with the following specifications:

It should accept the employee’s name and salary.
It should display both the name and salary.
If the salary is not provided in the function call, it should default to 9000.
"""

def show_employee(name, salary=9000):
    print("Name:", name, "salary:", salary)

show_employee("John", 12000)
show_employee("Josh")

"""
Exercise 5: Create an inner function

Create a program with nested functions to perform an addition calculation as follows:

Define an outer function that accepts two parameters, a and b.
Inside this outer function, define an inner function that calculates the sum of a and b.
The outer function should then add 5 to this sum.
Finally, the outer function should return the resulting value.”
"""

def outer(a, b):
    square = a ** 2

    def addition(a, b):
        return a + b
    
    add = addition(a, b)

    return add + 5

res = outer(5, 10)
print(res)

"""
Exercise 6: Create a recursive function

Write a program to create a recursive function that calculates the sum of numbers from 0 to 10.

A recursive function is a function that calls itself repeatedly.

Expected Output:

55
"""

def addition(num):
    if num:
        return num + addition(num - 1)
    else:
        return 0
    
res = addition(10)
print(res)
    
"""
Exercise 1: Generate 3 Random Integers

Write a code to generate 3 random integers between 100 and 999 which is divisible by 5
"""
import random
for num in range(3):
    print(random.randrange(100, 999, 5), end=", ")

"""
Exercise 2: Random Lottery Pick

Write a code to generate 100 random lottery tickets and pick two lucky tickets from it as a winner.
"""
lottery = []
for i in range(100):
    lottery.append(random.randrange(1000, 9999))
winners = random.sample(lottery, 2)
print(winners)