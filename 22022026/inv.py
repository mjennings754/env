# based from interview on google docs

# create a list and a tuple
list1 = [1, 2, 3, 4]

tuple1 = (1, 2, 3)
print(list1, tuple1)

#reverse a tuple
print(tuple1[::-1])

#add the the tuple *
#tuple1.add(2)
#print(tuple1)
#* tuples are immutable, you'll have to create a new tuple

# create a list using comprehension
my_list = [i for i in range(10)]
print(my_list)  

# how to do you write?

try:
    with open('file.txt', 'r') as file:
        file.read
except:
    with open('file.txt', 'w') as file:
        file.read

# what are decorators?
# with decorators, you can add functionality to an existing function without
# having to create a new one

def changecase(func):
    def wrapper():
        text = func()
        if text:
            for char in text:
                print(char.upper(), end="")
        else:
            print("No text")
    return wrapper


@changecase
def add_text():
    return "Python is a high-level programming language"

add_text()

# create a docstring

def do_something():
    """
    This function does something...
    """
    pass

# what is dunder?
# double underscore __init__(self,.....)


# how to manage data
def large_dataset_generator(n):
    for i in range(n):
        yield i

print(large_dataset_generator(100))

# how can you concatenate two lists?
a = [1, 2, 3]
b = [4, 5, 6]
res = a + b
print(res)

