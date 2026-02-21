my_list = [i for i in range(1,10)]
print(my_list)

my_dict = {i: i**2 for i in range(1, 10)}
print(my_dict)

class monkey:
    def patch(self):
        print("patch() is being called")

def monk_p(self):
    print("monk_p() is being called")

monkey.patch = monk_p

obj = monkey()

obj.patch()