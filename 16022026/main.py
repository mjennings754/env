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
    