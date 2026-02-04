import random
range_list = [1, 100]
for i in range(random.randint(*range_list)): # * unpacks the elements of the list
    print(i)

shopping_list = []
item = input("What item do you want to add? ")
shopping_list.append(item)
print(shopping_list)

