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