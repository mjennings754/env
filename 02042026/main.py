import random

def random_ipv6():
    return ":".join(f"{random.randint(0, 0xFFFF):04x}" for _ in range(8))

print(random_ipv6())