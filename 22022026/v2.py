# create a list

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# what is at the middle?
middle = len(list1) // 2
print(middle)

# reverse the list
print(list1[::-1])

# replace 7
list1[6] = 7.5
print(list1)
list1.extend([5, 6, 87, 8,4, 2])
print(list1)
 
# remove duplicates

list1 = set(list1)
list1 = list(list1)
print(list1)

# create a lambda to times itself by 2

duplicate = lambda x: x * 2
print(duplicate(2))