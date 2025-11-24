from functools import reduce

my_ints_a = [1, 2, 3, 4, 5] # range...
my_ints_b = [6, 7, 8, 9, 10] # range...

result = reduce(lambda a, b: a * b, my_ints_a)
print(result)

result = reduce(lambda a, b: a * b, my_ints_b)
print(result)