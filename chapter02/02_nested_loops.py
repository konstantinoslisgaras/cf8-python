print("Nested loops.")

for i in range(1, 3 + 1):
    for j in range(1, 11):
        print(f"{i} * {j} = {i * j}", end=" | ")
    print()
print()