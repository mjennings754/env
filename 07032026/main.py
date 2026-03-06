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