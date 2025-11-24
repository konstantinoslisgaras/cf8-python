numbers = [2, 4, 7, 11, 13]

number_to_find = 7
i = 0

while i < len(numbers):
    if numbers[i] == number_to_find:
        print("Found:", number_to_find)
        break
    i += 1
else:
    print("Target not found.")
