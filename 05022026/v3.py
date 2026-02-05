class Player():
    stats = {"Attack": 99, "Strength:":89, "Defense": 95, "Range": "76", "Magic": 88, "Prayer": 77}
    def __init__(self, username, members, max_hit, health, mod):
        self.username = username
        self.members = members
        self.max_hit = max_hit
        self.health = health
        self.mod = mod

    @classmethod
    def show_player_stats(cls):
        return Player.stats

ZhenHen = Player("Zhen hen", True, "48", 99, False)

print(ZhenHen.stats)
print(vars(ZhenHen))

class Parrot:
    def __init__(self):
        self._voltage = 10000

    @property
    def voltage(self):
        return self._voltage

p = Parrot()

print(p.voltage)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # __repr__ returns a string containing a printable representation of an object
    def __repr__(self):
        return f"Person('{self.name}', {self.age})"
    
p = Person("Mitchell", 26)
print(p)