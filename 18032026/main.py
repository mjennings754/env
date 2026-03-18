# add some list comprehension

words = ["apple", "bat", "cherry", "dog", "elderberry"]
newlist = [word.upper() for word in words if len(word) >= 4]
print(newlist)

# flatten a nested list


def flatten(lst):
    flat_list = []

    for item in lst:
        if isinstance(item, list):
            flat_list.extend(flatten(item))
        else:
            flat_list.append(item)

    return flat_list

nested = [1, [2, 3], [4, [5, 6]], 7]
res = flatten(nested)
print(res)