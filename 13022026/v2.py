# remove occurences of a number in a list
list1 = [5, 4, 3, 21, 23, 45, 68, 76, 20, 20 ,20]
while 20 in list1:
    list1.remove(20)
print(list1)

# use list comprehension to create a new list containing only numbers

mixed = [1, 4, 5, 'Random', 6, 8, 'Random2', 4.5]

numbers = [item for item in mixed if isinstance(item, (int, float))]
print(numbers)