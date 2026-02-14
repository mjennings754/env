"""
Exercise 8. String Reversal

Practice Problem: Write a program that takes a string and reverses it (e.g., “Python” becomes “nohtyP”).
"""
text = "Python"
print(text[::-1])

"""
Exercise 9. Vowel Frequency Counter

Practice Problem: Write a program to count the total number of vowels (a, e, i, o, u) present in a given sentence.
"""
sentence = "Learning Python is fun!"
vowels = "aeiou"
count = 0
for char in sentence.lower():
    if char in vowels:
        count += 1

print(count)

"""
Exercise 10. Finding Extremes (Min/Max) in a List

Practice Problem: Given a list of integers, find and print both the largest and the smallest numbers.

"""
nums = [45, 2, 89, 12, 7]

max = max(nums)
print(max)
min = min(nums)
print(min)

"""
Exercise 11. Removing Duplicates from a List

Practice Problem: Write a script that takes a list containing duplicate items and returns a new list with only unique elements.
"""
data = [1, 2, 2, 3, 4, 4, 4, 5]
data = set(data)
print(data)

"""
Exercise 15. Nested Loops for Pattern Generation

Practice Problem: Print the following pattern where each row contains a number repeated a specific number of times based on its value.
"""
for num in range(1, 6):
    for i in range(num):
        print(num, end=" ") 
    print("\n")


"""
Exercise 16. Numerical Palindrome Check

Practice Problem: Write a program to check if a given number is a palindrome (reads the same forwards and backwards).
"""

def is_palindrome(x):
    org = str(x)
    reversed = org[::-1]

    if org == reversed:
        print("Yes")
    else:
        print("No")

is_palindrome(121)
is_palindrome(125)