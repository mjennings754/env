class Player:
    def __init__(self, name, health, dps, player_class=str):
        self.name = name
        self.health = health
        self._dps = dps
        self._player_class = player_class

    def display_info(self):
        print(f"Player name: {self.name}")
        print(f"Health: {self.health}")
        print(f"DPS: {self._dps}")
        print(f"What class? {self._player_class}")

    @classmethod
    def user_input(cls):
        name = input("Enter your name: ")
        health = input("Enter your health: ")
        dps = input("Enter your Damage Per Second: ")
        player_class = input("Enter your class: ")
        return cls(name, health, dps, player_class)

    @property
    def dps(self):
        return f"{self._dps}"
    
player1 = Player.user_input()
print(player1.dps)


