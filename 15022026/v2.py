list1 = [1, 2, 3, "hello", 4, 5, 6]

newlist = [item for item in list1 if isinstance(item, (int))]
print(newlist)

a = [10, 20, 30, 40]    
b = [100, 200, 300, 400]

for x, y in zip(a, b[::-1]):
    print(x, y) 

"""
Exercise 1A: Create a string made of the first, middle and last character
"""

str1 = "James"
first = str1[0]
res = str1[0]
l = len(str1)
mi = int(l / 2)
res = res + str1[mi]
res = res + str1[l - 1]
print(res)

"""
Exercise 2: Append new string in the middle of a given string

Given two strings, s1 and s2. Write a program to create a new string s3 by appending s2 in the middle of s1.
"""
s1 = "Ault"
s2 = "Kelly"

middle = int(len(s1) / 2)

x = s1[:middle:]
x = x + s2
x = x + s1[mi:]

print(x)

"""
Exercise 1: Perform Basic Tuple Operations

Create a Tuple: Create a tuple named my_tuple containing the numbers 1, 2, 3, 4, and 5.
Access Elements: Access and print the third element of my_tuple.
Tuple Length: Find and print the length of my_tuple.
"""

my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[3])
print(len(my_tuple))

"""
Exercise 2: Tuple Repetition

Repeat a below tuple three times.
"""

original_tuple = ('a', 'b')

print(original_tuple * 3)

"""
Exercise 3: Slicing Tuples

Slice below tuple to get elements from the 4th to the 7th position.
"""
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print(numbers[3:7])

"""
Exercise 4: Reverse the tuple
"""
tuple1 = (10, 20, 30, 40, 50)

print(tuple1[::-1])