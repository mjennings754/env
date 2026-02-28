"""
Exercise 1: List Comprehension Mastery

Practice Problem: Write a single-line list comprehension that takes a list of strings, filters out strings shorter than 4 characters, and converts the remaining strings to uppercase.
Given Input: words = ["apple", "bat", "cherry", "dog", "elderberry"]

Expected Output: ['APPLE', 'CHERRY', 'ELDERBERRY']
"""
words = ["apple", "bat", "cherry", "dog", "elderberry"]

list1 = [word.upper() for word in words if len(word) >= 4]
print(list1)