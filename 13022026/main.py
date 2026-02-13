"""
my_list = [10, 20, 30, 40, 50]
Perform following operations on given list

Access Elements: Print the third element.
List Length: Print the number of elements in the list
Check if Empty: Write a code to check is list empty.


Expected Output:

Initial list: [10, 20, 30, 40, 50]

Third item:  30
Length of the list: 5
list is not empty

"""

list = [10, 20, 30, 40, 50]
print(f"Initial list: {list}")
print(f"Third item: {list[2]}")
print(f"Lenth of the list: {len(list)}")
if list is None:
    print("random")
else:
    print("list is not empty")

"""
Exercise 2: Perform List Manipulation

Given:

my_list = [10, 20, 30, 40, 50]
Perform following list manipulation operations on given list

Change Element: Change the second element of a list to 200 and print the updated list.
Append Element: Add 600 o the end of a list and print the new list.
Insert Element: Insert 300 at the third position (index 2) of a list and print the result.
Remove Element (by value): Remove 600 from the list and print the list.
Remove Element (by index): Remove the element at index 0 from the list print the list.
Expected Output:

Initial list: [10, 20, 30, 40, 50]

After changing second element: [10, 200, 30, 40, 50]
List after appending 600: [10, 200, 30, 40, 50, 600]
List after inserting 300 at index 2: [10, 200, 300, 30, 40, 50, 600]
List after removing 600 (by value): [10, 200, 300, 30, 40, 50]
List after removing element at index 0: [200, 300, 30, 40, 50]
"""

list = [10, 20, 30, 40, 50]
list[1] = 200
print(f"After changing second element: {list}")
list.append(600)
print(f"List after appending 600: {list}")
list.insert(2, 300)
print(f"List after inserting 300 at index 2: {list}")
list.remove(600)
print(f"List after removing 600 (by value): {list}")
del list[0]
print(f"List after removing element at index 0: {list}")