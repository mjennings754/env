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