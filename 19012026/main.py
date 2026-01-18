# Create a for loop to go through 0 to 10
for i in range(11):
    print(i)

# do tuple unpacking
box = {'tape', 'cardboard box', 'postage label'}
a, b, c = box
print(a)
print(b)
print(c)

# Create a decorator
def changecase(func):
    def myinner():
        return func().upper()
    return myinner

@changecase
def myfunction():
    return "This should all be uppercase"

print(myfunction())