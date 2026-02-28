"""
Exercise 1: List Comprehension Mastery

Practice Problem: Write a single-line list comprehension that takes a list of strings, filters out strings shorter than 4 characters, and converts the remaining strings to uppercase.
Given Input: words = ["apple", "bat", "cherry", "dog", "elderberry"]

Expected Output: ['APPLE', 'CHERRY', 'ELDERBERRY']
"""
words = ["apple", "bat", "cherry", "dog", "elderberry"]

list1 = [word.upper() for word in words if len(word) >= 4]
print(list1)

"""
Exercise 2: Dictionary Merging with Logic

Practice Problem: Write a function that merges two dictionaries. If a key exists in both dictionaries, sum their values. If a key exists in only one, include it as is.
Given Input: dict_a = {'a': 10, 'b': 20} dict_b = {'b': 5, 'c': 15}

Expected Output: Merged Dictionary: {'a': 10, 'b': 25, 'c': 15}
"""
def merge(dict_a, dict_b):
    res = dict_a.copy()

    for key, value in dict_b.items():
        res[key] = res.get(key, 0) + value
    return res
dict_a = {'a': 10, 'b': 20} 
dict_b = {'b': 5, 'c': 15}

merged = merge(dict_a, dict_b)
print(merged)

"""
Exercise 3: Frequency Map with Counter

Practice Problem: Create a function that takes a string and returns a count of how many times each character appears. Ignore spaces and make it case-insensitive.
"""
from collections import Counter
def get_count(x):
    clean_str = x.lower().replace(" ", "")

    return Counter(clean_str)
        
text = "Python Programming"
freq = get_count(text)
print(freq)