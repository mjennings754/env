# add some list comprehension

words = ["apple", "bat", "cherry", "dog", "elderberry"]
newlist = [word.upper() for word in words if len(word) >= 4]
print(newlist)