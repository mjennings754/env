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