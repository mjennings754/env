list1 = [1, 2, 3, "hello", 59.0, "testing"]
print(list1)
newlist = [item for item in list1 if isinstance(item, (int))]
print(newlist)

