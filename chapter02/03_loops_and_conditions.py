print("1 - 9, step:3")

for i in range(1, 10, 3):
    print(i, end=" ")
print()

print("0 - 9, break:5")
for i in range(10):
    if i == 5:
        break
    print(i, end=" ")
print()

print("0 - 9, skip:5")
for i in range(10):
    if i == 5:
        continue
    print(i, end=" ")
print()

# For loop can contain else block
for i in range(10):
    if i == 50:
        break
    print(i, end=" ")
else:
    print(" - Loop ended normally.")

fruits = ["Mango", "Avocado", "Peach", "Tomato"]

fruit_to_check = "Avocado"

# Method 1
for fruit in fruits:
    if fruit == fruit_to_check:
        print(f"Fruit {fruit_to_check} exists!")
        break
else:
    print(f"Fruit {fruit_to_check} do not exist!")

print("Why do Python developers never get lost?")
print("Because they always know where 'in' is!")

# Method 2
if fruit_to_check in fruits:
    print(f"Fruit {fruit_to_check} exists!")
else:
    print(f"Fruit {fruit_to_check} do not exist!")

# Method 3 - Conditional check
print("=" * 50)
print(f"{fruit_to_check} is {'in' if fruit_to_check in fruits else 'not in'} in the fruit list!")