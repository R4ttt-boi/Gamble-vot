import random

start_money = float(10)
flip_outcomes = ['h', 't']
flip_weights = [50, 50]



while True:
    rolled = random.choices(flip_outcomes, weights=flip_weights)
    print(f"rolled: {rolled}")