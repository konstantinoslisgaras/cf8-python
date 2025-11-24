numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # list(range(1, 10 + 1))

even_numbers_iterator = filter(lambda x: x % 2 == 0, numbers)
print(type(even_numbers_iterator))

# print(*even_numbers_iterator) # Unpacking

for num in even_numbers_iterator:
    print(num, sep=" | ", end=" ")
    if num == 4:
        break
print()

print("="*10)

for num in even_numbers_iterator:
    print(num, sep=" | ", end=" ")
    print()

#
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print("Repeated print of the even numbers list:")
print(even_numbers)
print(even_numbers)