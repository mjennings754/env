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