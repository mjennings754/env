list1 = [1, 2, 3, "hello", 59.0, "testing"]
print(list1)
newlist = [item for item in list1 if isinstance(item, (int))]
print(newlist)

list2 = [1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 9, 0]

while 5 in list2:
    list2.remove(5)
print(list2)