list1 = [1, 2, 3, "hello", 4, 5, 6]

newlist = [item for item in list1 if isinstance(item, (int))]   

print(newlist)

