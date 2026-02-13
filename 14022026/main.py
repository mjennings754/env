"""
Exercise 1: List Comprehension Mastery

Practice Problem: Write a single-line list comprehension that takes a list of strings, filters out strings shorter than 4 characters, and converts the remaining strings to uppercase.
"""

words = ["apple", "bat", "cherry", "dog", "elderberry"]

newlist = [w.upper() for w in words if len(w) >= 4]
print(newlist)

"""
Exercise 2: Dictionary Merging with Logic

Practice Problem: Write a function that merges two dictionaries. If a key exists in both dictionaries, sum their values. If a key exists in only one, include it as is.
"""
dict_a = {'a': 10, 'b': 20} 
dict_b = {'b': 5, 'c': 15}

def merge_dicts(d1, d2):
    result = d1.copy()

    for key, value in d2.items():
        result[key] = result.get(key, 0) + value

    return result
merged = merge_dicts(dict_a, dict_b)
print(merged)