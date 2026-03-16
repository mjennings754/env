"""
Exercise 16: Use a lambda with the map() function to double each element in a list
"""
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)

"""
Exercise 17: Use a lambda with the sorted() function to sort a list of tuples based on the second element
"""
data = [('apple', 5), ('banana', 2), ('cherry', 8), ('date', 1)]
sorted = sorted(data, key=lambda item: item[1])
print(sorted)

"""
Exercise 3: Dictionary from Lists
"""

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

res = dict(zip(keys, values))
print(res)