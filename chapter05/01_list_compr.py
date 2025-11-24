list_of_ints = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# 1. Using list comprehension to square every number in the list.
squared_list_compr = [number ** 2 for number in list_of_ints]
print("Squared list comprehension:", squared_list_compr)

# 2. Using map with a lambda to square every number in the list.
squared_map_lambda = list(map(lambda x: x ** 2, list_of_ints))
print("Squared with lambda:", squared_map_lambda)

# 3. Function definition and list comprehension to square every number in the list.
def square_function(number):
    return number ** 2

squared_list_func = [square_function(num) for num in list_of_ints]
print("Squared with function:", squared_list_func)

# 4. List comprehension with filtering and mapping.
squared_filtered_numbers = [number ** 2 for number in list_of_ints if number % 2 != 0]
print("Squared filtered numbers:", squared_filtered_numbers)

# 5. Squared numbers using filter and map built-in functions.
squared_filtered_map_func = list(map(square_function, filter(lambda x: x % 2 != 0, list_of_ints)))
print("Squared filtered map function:", squared_filtered_map_func)

# 6. Squared numbers using 2 lambdas as predicates.
squared_filtered_map_lambdas = list(map(lambda x: x ** 2, filter(lambda x: x % 2 != 0, list_of_ints)))
print("Squared filtered using lambdas:", squared_filtered_map_lambdas)