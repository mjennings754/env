for i in range(10):
    i += 1
    print(i)

for _ in range(10):
    print("[x]" * _)
for _ in range(20):
    print("[O]" * _)

for _ in range(10):
    print(_ * "[x]")

for _ in range(15):
    print("[x]" * _)

height = 9
for i in range(1, height + 1):
    print((" " * 3) * (height - i) + "[x]" * i)
for _ in range(10):
    print("[x]" * _)

for i in range(1, height + 1):
    spaces = " " * (height - i)
    blocks = "[x]" * i
    print(spaces + blocks)
"""
import random
number = random.randint(1, 10)
guess = int(input("What number am I thinking ?"))
while guess != number:
    if guess > number:
        print("Too High")
    else:
        print("Too low")
    guess = int(input("Try again: "))

print("Correct!")
"""

numbers = ["4", "5", "3", "10", "12"]

print(numbers[::-1])