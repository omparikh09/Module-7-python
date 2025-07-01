"""
Write a Python program to generate random numbers using the random module.
"""

import random

random_int = random.randint(1000,9999)
print(f"Random Integer :- {random_int}")

random_float = random.random()
print(f"Random Float :- {random_float}")

random_uniform = random.uniform(10,50)
print(f"Random Uniform :- {random_uniform}")

num = [10, 20, 30, 40, 50]
random_choice = random.choice(num)
print(f"Random Choice form list :- {random_choice}")

random.shuffle(num)
print(f"Shuffle List :- {num}")