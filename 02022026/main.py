for i in range(5):
    print(i)

class Player():
    def __init__(self, health):
        self.health = health

player = Player(100)

print(vars(player))

empty_tuple = ()
print(empty_tuple)
empty_tuple = ("test", "testing", "tester")
print(empty_tuple)

number_list = []
for number in range(1, 6):
    number_list.append(number)

print(number_list)

number_thing = (number for number in range(1, 6))

print(number_thing)

dictionary = {'hello':'こんにちは', 'thank you':'ありがとう', 'have a nice day':'良い１日を'}
for english, japanese in dictionary.items():
    print(f"{english}:{japanese}")

def capitalize(words, func):
    for word in words:
        print(func(word))

double = lambda x: x * 2
add = lambda x, y: x + y
print(double(2))
print(add(4, 5))
max_value = lambda x, y: x if x > y else y
min_value = lambda x, y: x if x < y else y
print(max_value(4, 5))
print(min_value(8, 7))
full_name = lambda first, last: first + " " + last
print(full_name("Spongebob", "Squarepants"))

is_even = lambda x: x % 2 == 0

print(is_even(7))