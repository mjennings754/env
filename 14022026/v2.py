"""
Exercise 1. Arithmetic Product and Conditional Logic

Practice Problem: Write a Python function that accepts two integer numbers. If the product of the two numbers is less than or equal to 1000, return their product; otherwise, return their sum.

Exercise Purpose: Learn basic control flow and the use of if-else statements. Understand how code decisions change output based on a mathematical threshold.

Given Input:

Case 1: number1 = 20, number2 = 30
Case 2: number1 = 40, number2 = 30
Expected Output:

The result is 600
The result is 70

"""

def calculate(num1, num2):
    res = int(num1 * num2)
    if res <= 1000:
        return res
    else:
        return sum(res)
print(calculate(20, 30))

def addition(num1, num2):
    print(num1 + num2)

addition(40, 30)

"""
Exercise 2. Cumulative Sum of a Range

Practice Problem: Iterate through the first 10 numbers (0–9). In each iteration, print the current number, the previous number, and their sum.

Exercise Purpose: This exercise teaches “State Tracking.” In programming, you often need to remember a value from a previous loop iteration to calculate results in the current one. This is the basis for algorithms like Fibonacci sequences or running totals.

Given Input: Range: numbers = range(10)
"""

print("Printing current and previous number sum in a range(10)")
prev_num = 0

for i in range(10):
    x_sum = prev_num + i
    print(f"Current number {i} Previous Number {prev_num} Sum: {x_sum}")

    prev_num = i