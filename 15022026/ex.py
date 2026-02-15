"""
Exercise 1: Generate 3 Random Integers

Write a code to generate 3 random integers between 100 and 999 which is divisible by 5
"""
# need to import random
import random

# 3 random integers, so range(3)
for i in range(3):
    #generate between 100 and 999
    print(random.randrange(100, 999, 5), end=", ")

"""
Exercise 2: Random Lottery Pick

Write a code to generate 100 random lottery tickets and pick two lucky tickets from it as a winner.
"""
lottery_tickets = []
for i in range(100):
    lottery_tickets.append(random.randrange(1000, 9999))
winners = random.sample(lottery_tickets, 2)

print(winners)

"""
Exercise 9. Vowel Frequency Counter

Practice Problem: Write a program to count the total number of vowels (a, e, i, o, u) present in a given sentence.
"""

count = 0
vowels = 'aeiou'
word = "Programming Python"
for char in word:
    if char in vowels:
        count += 1

print(count)

# find all the integers in a list

list1 = [1, 2, 3, "word", "word2", 94, 34.0]
newlist = [item for item in list1 if isinstance(item, (int))]
print(newlist)

# check palindrome

def check(x):
    x = str(x)
    reversed = x[::-1]
    if reversed == x:
        print("True")
    else:
        print("False")

check(102)


# remove duplicates

list2 = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 6, 6, 6, 6, 7, 7, 7, 8, 9, 9, 9, 10]

list3 = set(list2)
print(list3)

# remove number 5

list2 = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 6, 6, 6, 6, 7, 7, 7, 8, 9, 9, 9, 10]

while 5 in list2:
    list2.remove(5)

print(list2)