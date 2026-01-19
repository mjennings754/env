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