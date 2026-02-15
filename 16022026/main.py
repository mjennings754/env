list1 = [1, 2, 3, "hello", 4, 5, 6]

newlist = [item for item in list1 if isinstance(item, (int))]   

print(newlist)

"""
Exercise 1: Perform Basic List Operations

Perform following operations on given list

Access Elements: Print the third element.
List Length: Print the number of elements in the list
Check if Empty: Write a code to check is list empty.
"""

my_list = [10, 20, 30, 40, 50]

print(my_list[2])
print(len(my_list))
if my_list is None:
    print("Empty")
else:
    print("list is not empty")

"""
Change Element: Change the second element of a list to 200 and print the updated list.
Append Element: Add 600 o the end of a list and print the new list.
Insert Element: Insert 300 at the third position (index 2) of a list and print the result.
Remove Element (by value): Remove 600 from the list and print the list.
Remove Element (by index): Remove the element at index 0 from the list print the list.

"""

my_list = [10, 20, 30, 40, 50]

my_list[1] = 200
print(my_list)
my_list.append(600)
print(my_list)
my_list.insert(2, 300)
print(my_list)
my_list.remove(600)

del my_list[0]
print(my_list)

"""
Calculate and print the sum and average of all numbers in a list.
"""
my_list = [10, 20, 30, 40, 50]
print(sum(my_list))
print(sum(my_list) / len(my_list))

"""
Given a list of numbers. write a program to turn every item of a list into its square.
"""

numbers = [1, 2, 3, 4, 5, 6, 7]

res = []

for n in numbers:
    res.append(n * n)
print(res)

"""
Find and print the largest and smallest number in a list [8, 2, 15, 1, 9].
"""

data = [8, 2, 15, 1, 9]

max = max(data)
min = min(data)

print(max, min)

"""
Sort a given list of numbers in ascending order and print it.
"""
numbers = [5, 2, 8, 1, 9]
numbers.sort()
print(numbers)