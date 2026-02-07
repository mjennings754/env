"""import json
game = []
name_input = input("What's the name of the game? ")
genre_input = input("What's the genre? ")
release_date_input = input("What's the release date? ")
game_input = name_input, genre_input, release_date_input
game.append(game_input)
with open('game.json', 'w') as f:
    json.dump(game, f)

print(game)"""

class Student():
    count = 0
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1

    @classmethod
    def get_count(cls):
        return f"The current count is {Student.count}"
    

student1 = Student("name", 4.8)
print(Student.get_count())


class Temperature:
    def __init__(self, celsius):
        self._calcius = celsius

    @property
    def celsius(self):
        return self._calcius
    
    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temp below absolute zero")
        self._celsius = value

t = Temperature(25)
print(t.celsius)
