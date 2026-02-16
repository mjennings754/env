list1 = [1, 2, 3, 4, "hello"]
newlist = [item for item in list1 if isinstance(item, int)]

print(newlist)

list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(list2[::-2])

"""
Exercise 26. Merging Two Dictionaries

Practice Problem: Write a program that takes two separate dictionaries and merges them into one single dictionary.
"""

dict1 = {"name": "Alice", "age": 25}
dict2 = {"city": "New York", "job": "Engineer"}

dict3 = dict1 | dict2
print(dict3)

"""
Exercise 27. Finding Common Elements (Intersections)

Practice Problem: Take two lists and find the elements that appear in both. Use Sets to perform the operation.
"""
list_a = [1, 2, 3, 4, 5]
list_b = [4, 5, 6, 7, 8]

set_a = set(list_a)
set_b = set(list_b)
common = set_a & set_b
print(common)