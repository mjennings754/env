# create a list

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# what is at the middle?
middle = len(list1) // 2
print(middle)

# reverse the list
print(list1[::-1])

# replace 7
list1[6] = 7.5
print(list1)
list1.extend([5, 6, 87, 8,4, 2])
print(list1)
 
# remove duplicates

list1 = set(list1)
list1 = list(list1)
print(list1)

# create a lambda to times itself by 2

duplicate = lambda x: x * 2
print(duplicate(2))

# insert into the list at the fist index
list1.insert(1, 10)
print(list1)

# create a simple decorator

def add_lights(func):
    def wrapper():
        print("* You turn the lights on")
        func()
    return wrapper

@add_lights
def xmas_tree():
    print("You see a Christmas Tree")

xmas_tree()

# do multiple inheritance

class Macbook:
    def processor(self):
        return "Macbook processor"
    
class Apple(Macbook):
    def processor(self):
        return "Apple processor"
    
Apple = Apple()
Apple2 = Macbook()
print(Apple.processor())
print(Apple2.processor())