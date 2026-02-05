class Player():
    count = 0 

    def __init__(self, name):
        self.name = name
        Player.count += 1

    @classmethod
    def get_count(cls):
        return f"The current player count is: {Player.count}"

# With classmethod you don't need to have an instance
print(Player.get_count())