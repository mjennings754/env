list1 = [1, 2, 3, "hello"]
newlist = [item for item in list1 if isinstance(item, (int))]

print(newlist)

"""
Exercise 1: List Comprehension Mastery

Practice Problem: Write a single-line list comprehension that takes a list of strings, filters out strings shorter than 4 characters, and converts the remaining strings to uppercase.
"""
words = ["apple", "bat", "cherry", "dog", "elderberry"]
newlist1 = [item.upper() for item in words if len(item) >= 4]
print(newlist1)


"""
Exercise 2: Dictionary Merging with Logic

Practice Problem: Write a function that merges two dictionaries. If a key exists in both dictionaries, sum their values. If a key exists in only one, include it as is.
"""

dict_a = {'a': 10, 'b': 20} 
dict_b = {'b': 5, 'c': 15}

def merge_dict(d1, d2):
    result = d1.copy()

    for key, value in d2.items():
        result[key] = result.get(key, 0) + value

    return result

merged = merge_dict(dict_a, dict_b)
print(merged) 


"""
Exercise 6: Reverse Each Word of a String

Practice Problem: Given a sentence, reverse each individual word within the string while maintaining the original word order.
"""

sentence = "Python is awesome"

def reverse_word(sentence):
    words = sentence.split()

    reversed_words = [word[::-1] for word in words]

    return " ".join(reversed_words)
text = "Python is awesome"
print(reverse_word(text))