"""
Exercise 7: Palindrome Sentence

Practice Problem: Write a function to check if a full sentence is a palindrome. You must ignore case, spaces, and all punctuation marks.
"""

def is_palindrome(x):
    x = str(x)
    original = str(x)
    reversed = x[::-1]
    if original == reversed:
        print(True)
    else:
        print(False)

is_palindrome(121)

"""
Exercise 8: List Comprehension Filtering (Advanced)

Practice Problem: Given a list of strings, use a single list comprehension to extract strings that meet two criteria: they must be longer than 5 characters AND they must start with a vowel (a, e, i, o, u).
"""
vowels = 'aeiou'
list1 = ["apple", "education", "ice", "ocean", "python", "umbrella"]
newlist1 = [word for word in list1 if len(word) > 5 and word[0].lower() in vowels]
print(newlist1)

"""
Exercise 9: Remove Duplicates (Preserving Order)
"""
def remove_duplicates(items):
    seen = set()
    res = []

    for x in items:
        if x not in seen:
            res.append(x)
            seen.add(x)
    return res

nums = [1, 2, 2, 3, 1, 4, 2]
print(remove_duplicates(nums))

"""
Exercise 11: Dictionary Merging (Value Grouping)

Practice Problem: Merge two dictionaries. If they share a key, the new dictionary should store a list containing values from both dictionaries instead of overwriting the first one.
"""

def merge(dict1, dict2):
    combined = {}

    all_keys = set(dict1.keys()) | set(dict2.keys())

    for key in all_keys:
        values = []
        if key in dict1:
            values.append(dict1[key])
        if key in dict2:
            values.append(dict2[key])
        combined[key] = values

    return combined

d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
print(merge(d1, d2))