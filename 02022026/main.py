for i in range(5):
    print(i)

class Player():
    def __init__(self, health):
        self.health = health

player = Player(100)

print(vars(player))