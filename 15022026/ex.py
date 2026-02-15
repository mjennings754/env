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
