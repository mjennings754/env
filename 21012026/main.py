# generate a hex code
import random
letters = "abcdef"
numbers = "1234567890"

hex_chars = letters + numbers

length = 6
hex_value = ''.join(random.choice(hex_chars) for _ in range(length))

print(f"#{hex_value}")

# create a while loop
count = 10
while count <= 100:
    print(count)
    count += 1

# add a random answer to a question
import random
question = "What do you want to eat for dinner?"
places = ["Korean BBQ", "Pizza", "Burritos"]
choice = random.choice(places)
print(question)
print(choice)

# Use a generator comprehension
for thing in ('Got %s' % number for number in range(10)):
    print(thing)

# Dictionary comprehension

squares = {key: key*key for key in range(10)}
print(squares)