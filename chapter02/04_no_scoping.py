import random

random_numbers = []

for _ in range(10):
    num = random.randint(1, 100) # generates random number between 1 - 100
    random_numbers.append(num)

print(random_numbers)
print(num)