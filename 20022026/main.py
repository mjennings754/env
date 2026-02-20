"""
Exercise 1: Print first 10 natural numbers using while loop
"""
for i in range(11):
    print(i)

"""
Exercise 2: Print the following pattern

Write a Python code to print the following number pattern using a loop.
"""
rows = 5
for i in range(1, rows + 1, 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print("")