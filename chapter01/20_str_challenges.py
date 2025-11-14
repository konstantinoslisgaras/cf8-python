word = "Factory"
char = "*"

for i in range(len(word)):
    print(f"{word[i] * (i + 1)}")

print("=" * 14)

for i in range(len(word)):
    print(f"{word[i] * (i + 1) + (len(word) - (i + 1)) * char}")

print("=" * 14)

for num in range(17):
    print(num, end=" ")
print()

print(num)