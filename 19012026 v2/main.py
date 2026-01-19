# reverse a string
string = 'lorem ipsum'
print(string[::-1])
# iterate through a string and print each value
for char in string:
    print(char)
# get user id from os module
import os
print(os.getuid())
# Add some text to a file
test_string = "Enter Sandman (Remastered)"
file = open('metallica.txt', 'wt')
file.write(test_string)
file.close()
# get the current time
from datetime import datetime
print(datetime.now())
# get the middle of a list
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
mid = len(num_list) // 2
print(mid)
# get the last element of the list
last = num_list[-1]
print(last)
# reverse the list
reverse_list = num_list[::-1]
print(reverse_list)
# print the last three characters of a string
three = "string"
print(three[3:])
# sort an unsorted array
A = [2, 4, 3, 6, 7, 8, 4, 5, 9]

def bubble_sort(arr):
    n = len(arr)
    flag = True
    while flag:
        flag = False
        for i in range(1, n):
            if arr[i-1] > arr[i]:
                arr[i], arr[i-1] = arr[i-1], arr[i]
                flag = True

bubble_sort(A)
print(A)
# OR
print(sorted(A))

# define a class for a player for a video game
class Player():
    def __init__(self, health, dps, role):
        self.health = health
        self.dps = dps
        self.role = role

meiday = Player(4934, 352, "Mage")
print(vars(meiday))
# or you can have a __str__ method

# print the highest number from a list
num = [123, 456, 789]
high_num = max(num)
print(high_num)

# create a for loop that iterates through how many times from input
x = int(input("How many times to loop: "))
for i in range(x):
    print(i)