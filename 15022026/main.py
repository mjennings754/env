list1 = [1, 2, 3, "hello", "testing", 49.0]
newlist = [item for item in list1 if isinstance(item, (int))]

print(newlist)