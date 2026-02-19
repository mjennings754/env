list1 = [1, 2, 3, "hello"]
newlist = [item for item in list1 if isinstance(item, (int))]

print(newlist)

"""
Exercise 1: List Comprehension Mastery

Practice Problem: Write a single-line list comprehension that takes a list of strings, filters out strings shorter than 4 characters, and converts the remaining strings to uppercase.
"""
words = ["apple", "bat", "cherry", "dog", "elderberry"]
newlist1 = [item.upper() for item in words if len(item) >= 4]
print(newlist1)