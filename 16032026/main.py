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