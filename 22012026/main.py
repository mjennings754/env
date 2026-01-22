# generate a for loop
for i in range(10):
    print(i)

# do multiple inheritance

class Car:
    def transmission(self):
        return "Car transmission"
    
class Honda(Car):
    def transmission(self):
        return "Automatic transmission"
    
Honda = Honda()
print(Honda.transmission())

# properties for computed values
class Circle():
    def __init__(self, radius):
        self.radius = radius
    @property
    def diameter(self):
        return 2 * self.radius
    
print(Circle(10))

