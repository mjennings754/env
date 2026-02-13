"""
Exercise 1: List Comprehension Mastery

Practice Problem: Write a single-line list comprehension that takes a list of strings, filters out strings shorter than 4 characters, and converts the remaining strings to uppercase.
"""

words = ["apple", "bat", "cherry", "dog", "elderberry"]

newlist = [w.upper() for w in words if len(w) >= 4]
print(newlist)