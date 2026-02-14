list1 = [1, 2, 3, "hello", 59.0, "testing"]
print(list1)
newlist = [item for item in list1 if isinstance(item, (int))]
print(newlist)

list2 = [1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 9, 0]

while 5 in list2:
    list2.remove(5)
print(list2)

dict_a = {'a': 20}
dict_b = {'b': 30}

def merge_dict(dict1, dict2):
    res = dict1.copy()

    for key, value in dict2.items():
        res[key] = res.get(key, 0) + value

    return res

merged = merge_dict(dict_a, dict_b)
print(merged)

words = ["apple", "bat", "cherry", "dog", "elderberry"]

newlist = [char.upper() for char in words if len(char) >= 4]
print(newlist)