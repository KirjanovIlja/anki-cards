import random


def generate_int_id() -> int:
    return random.randint(1_000_000_000, 2_147_483_647)
