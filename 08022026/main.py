import random

class Boss:
    def __init__(self, combat_level, max_hit, health):
        self.combat_level = combat_level
        self.max_hit = max_hit
        self.health = health

class Player:
    kc = 0
    def __init__(self, combat_level, max_hit, health):
        self.combat_level = combat_level
        self.max_hit = max_hit
        self.health = health

    def attack(self):
        return random.randint(0, self.max_hit)
    
    @classmethod
    def add_kc(cls):
        cls.kc += 1
    
    def attack_boss(self, boss, attacks=10):
        for _ in range(attacks):
            damage = self.attack()
            boss.health -= damage
            print(f"Zezima hits Zulrah for {damage}. Zulrah HP: {boss.health}")

            if boss.health <= 0:
                print("Zulrah has been defeated")
                Player.add_kc()
                print(f"Zulrah kill count: {Player.kc}")
                break

Zulrah = Boss(725, 41, 500)
Zezima = Player(126, 76, 100)

Zezima.attack_boss(Zulrah)