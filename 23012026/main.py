list = []
for i in range(200, 3201):
    if (i%7==0) and (i%5!=0):
        list.append(i)

#print(list)

"""
Find PI to the Nth Digit - Enter a number and have the program generate PI up to that many decimal places.
Keep a limit to how far the program will go.
"""
import math
print(f"{math.pi:.9f}")

"""
Find e to the Nth Digit - Just like the previous problem, but with e instead of PI. Enter a number and have the program generate e up to that many decimal places. Keep a limit to how far the program will go.
"""
e = int(input("Enter a number: "))
print(f"{e:.{e}f}")

"""
Fibonacci Sequence - Enter a number and have the program generate the Fibonacci sequence to that number or to the Nth number.
"""

def fibonacci(n):
    a, b = 0, 1
    result = []
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result

print(fibonacci(10))

"""
Prime Factorization - Have the user enter a number and find all Prime Factors (if there are any) and display them.
"""
import math

def get_prime_factors(n):
    factors = []

    while n % 2 == 0:
        factors.append(2)
        n //= 2

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i
    
    if n > 2:
        factors.append(n)

    return factors

print(get_prime_factors(22))

"""
Find Cost of Tile to Cover W x H Floor - Calculate the total cost of tile it would take to cover a floor plan of width and height, using a cost entered by the user.
"""
"""
width = float(input("Enter the width: "))
height = float(input("Enter the height: "))
cost_per_unit = float(input("Enter a cost: "))

area = width * height

total_cost = area * cost_per_unit

print(total_cost)
"""
"""
Reverse a String - Enter a string and the program will reverse it and print it out.
"""

string = input("Enter a string: ")
print(string[::-1])


"""
Check if Palindrome - Checks if the string entered by the user is a palindrome. That is that it reads the same forwards as backwards like “racecar”
"""

def is_palindrome(s):
    cleaned = "".join(char.lower() for char in s if char.isalnum())

    return cleaned == cleaned[::-1]

input = input("Enter a word")

if is_palindrome(input):
    print("Yes")
else:
    print("No")

"""
Count Words in a String - Counts the number of individual words in a string. For added complexity read these strings in from a text file and generate a summary.
"""
def count_words_in_string(text):
    words = text.split()
    return len(words)

my_string = "Rock Paper Scissors Lizard Spock"
print(f"{count_words_in_string(my_string)}")