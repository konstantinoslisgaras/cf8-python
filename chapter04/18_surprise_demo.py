from functools import reduce

# Calculate factorial

n = int(input("Please enter a number to calculate its' factorial: "))

facto = reduce(lambda x, y: x * y, range(1, n + 1))
print(facto)

print("="*50)

def print_and_multiply(x, y):
    result = x * y
    print(f"{x} * {y} = {result}")
    return result

result = reduce(print_and_multiply, range(1, n + 1))

print("="*50)

final_result = reduce(lambda x, y: print(f"{x} * {y} = {x * y}") or x * y, range(1, n + 1))
print(final_result)