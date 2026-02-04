class Student:
    count = 0
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1

    @classmethod
    def get_count(cls):
        return f"The # of students {Student.count}"
    
Harry = Student("Harry", "3.9")

print(Student.get_count())

import random

class Player:
    locations = []
    possible_locations = ["Lumbridge", "Edgeville", "Varrock", "Falador"]

    def __init__(self, username, world):
        self.username = username
        self.world = world
        self.location = random.choice(Player.possible_locations)
        Player.locations.append(self.location)
        

    @classmethod
    def get_location(cls):
        return Player.locations
    
Zezima = Player("Zezima", "330")
    
print(Player.get_location())