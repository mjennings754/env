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

list22 = [10, 20, 30, 40, 50]
print(f"Initial list: {list22}")
print(f"Third item: {list22[2]}")
print(f"Lenth of the list: {len(list22)}")
if list22 is None:
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

list23 = [10, 20, 30, 40, 50]
list23[1] = 200
print(f"After changing second element: {list23}")
list23.append(600)
print(f"List after appending 600: {list23}")
list23.insert(2, 300)
print(f"List after inserting 300 at index 2: {list23}")
list23.remove(600)
print(f"List after removing 600 (by value): {list23}")
del list23[0]
print(f"List after removing element at index 0: {list23}")

"""
Exercise 3: Sum and average of all numbers in a list

Calculate and print the sum and average of all numbers in a list.

Given:

my_list = [10, 20, 30, 40, 50]
Expected Output:

Sum: 150
Average: 30.0
"""

list24 = [10, 20, 30, 40, 50]
print(f"Sum: sum(list24)")
average = sum(list24) / len(list24)
print("Average:", average)

"""
Exercise 4: Reverse a list
"""
list1 = [100, 200, 300, 400, 500]
print(list1[::-1])

"""
Exercise 5: Turn every item of a list into its square
"""
numbers = [1, 2, 3, 4, 5, 6, 7]

result = []
for n in numbers:
    result.append(n * n)
print(result)

"""
Exercise 6: Find Maximum and Minimum
"""

data = [8, 2, 15, 1, 9]

min = min(data)
print(min)
max = max(data)
print(max)

"""
Exercise 7: Count Occurrences

Count and print how many times 'Football' appears in list.
"""

sports = ['Cricket', 'Football', 'Hockey', 'Football', 'Tennis']

print(sports.count('Football'))

"""
Exercise 8: Sort a list of numbers
Sort a given list of numbers in ascending order and print it.

Given: numbers = [5, 2, 8, 1, 9]
"""
numbers = [5, 2, 8, 1, 9]
numbers.sort()
print(numbers)


"""
Exercise 9: Create a copy of a list

Create a copy of a list [10, 20, 30] and modify the copy. Print both the original and the copied list to demonstrate they are independent.
"""

list11 = [10, 20, 30]
copylist = list11.copy()
print(list11)
print(copylist)

"""
Exercise 10: Combine two lists

Combine given two lists into a single list and print it.
"""

list_a = [1, 2]
list_b = [3, 4]

newlist = list_a + list_b
print(newlist)

"""
Exercise 11: Remove empty strings from the list of strings
"""
list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
res = [x for x in list1 if x]
print(res)

"""
Exercise 12: Remove Duplicates from list

Write a function that takes a list with duplicate elements and returns a new list with only unique elements.
"""

list_with_duplicates = [1, 2, 2, 3, 1, 4, 5, 4]
unique_list = list(dict.fromkeys(list_with_duplicates))
print(unique_list)

"""
Exercise 13: Remove all occurrences of a specific item from a list

Given a Python list, write a program to remove all occurrences of item 20.
"""

list1 = [5, 20, 15, 20, 25, 50, 20]

while 20 in list1:
    list1.remove(20)
print(list1)

"""
Exercise 14: List Comprehension for Numbers

Use list comprehension to create a new list containing only the numbers from a given list.

"""

mixed_list = [1, 2, 3, 'Jessa', 4, 5, 'Kelly', 'Jhon', 6]

numbers_only = [item for item in mixed_list if isinstance(item, (int, float))]

print(numbers_only)

"""
Exercise 15: Access Nested Lists

Given a nested list, print the element '55'.
"""

nested_list = [[10, 20, 30], [44, 55, 66], [77, 87, 99]]

element55 = nested_list[1][1]

print(element55)