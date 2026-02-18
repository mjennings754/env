list1 = [1, 2, 3, "hello", "testing", 8, 9, 10]
newlist = [item for item in list1 if isinstance(item, int)]

print(newlist)

"""
Exercise 1: Print first 10 natural numbers using while loop
"""
for i in range(11): 
    print(i)

"""
Exercise 2: Print the following pattern
"""
row = 5
for i in range(1, row + 1, 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print("")