"""
Declare a function add_two_numbers. It takes two parameters and it returns a sum.
"""

def add_two_numbers(a, b):
    return a + b

print(add_two_numbers(10, 12))

"""
Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
"""
import math
def area_of_circle(r):
    area = math.pi * r * r
    return area

radius = 12
area = area_of_circle(radius)
print(area)

"""
Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
"""
def convert_celsius_to_fahrenheit():
    celsius = int(input("Enter celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(fahrenheit)

convert_celsius_to_fahrenheit()

"""
Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
"""
def check_season(month):
    if input == "March" or "April" or "May":
        print("Spring")
    elif input == "June" or "July" or "August":
        print("Summer")
    elif input == "September" or "October" or "November":
        print("Autumn")
    elif input == "December" or "January" or "February":
        print("Winter")

check_season("April")


"""
Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
"""
def print_list(x):
    list = []
    for i in range(x):
        list.append(i)
    return list

print(print_list(10))