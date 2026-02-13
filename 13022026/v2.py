# remove occurences of a number in a list
list1 = [5, 4, 3, 21, 23, 45, 68, 76, 20, 20 ,20]
while 20 in list1:
    list1.remove(20)
print(list1)

# use list comprehension to create a new list containing only numbers

mixed = [1, 4, 5, 'Random', 6, 8, 'Random2', 4.5]

numbers = [x for x in mixed if isinstance(x, (int))]
print(numbers)

nested = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print5 = nested[1][1]
print(print5)

"""
write a function to flatten a list of lists into a single list
"""
list_of_lists = [[1, 2], [3, 4], [5, 6, 7]]
def flatten(nested):
    return [item for sublist in nested for item in sublist]

res = flatten(list_of_lists)
print(res)

"""
concatenate two lists in the following order

Expected output:

['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']

"""
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
res = [x + y for x in list1 for y in list2]
print(res)