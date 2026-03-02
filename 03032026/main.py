# display the current time
import datetime
now = datetime.datetime.now()

print(now.strftime("%Y-%m-%d %H:%M:%S"))

# calcuate the area of a circle based on the radius input
from math import pi

r = float(input("Enter the radius: "))

area = pi * r ** 2

print(area)