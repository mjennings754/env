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