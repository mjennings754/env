for i in range(10):
    print(i)

DPS = 10000

class Player():
    def __init__(self, health, username, dps, max_hit):
        self.health = health
        self.username = username
        self.dps = dps
        self.max_hit = max_hit

player = Player(100, "sleepyfans", DPS, 100)
print(vars(player))
