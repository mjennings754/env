# display the current time
import datetime
now = datetime.datetime.now()

print(now.strftime("%Y-%m-%d %H:%M:%S"))

# calcuate the area of a circle based on the radius input
from math import pi

r = float(input("Enter the radius: "))

area = pi * r ** 2

print(area)

# reverse a full name from input
first = input("Enter your first name: ")
last = input("Enter your last name: ")
reversed = (f"{first[::-1]} {last[::-1]}")
print(reversed)