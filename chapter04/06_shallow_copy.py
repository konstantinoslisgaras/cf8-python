my_list = [1, 2, "Hello", [3, 4, 5]]

new_list = my_list

print("Are new_list and my_list the same object?:", my_list is new_list)

print(id(my_list))
print(id(new_list))

# Shallow copy
new_list = my_list[:]
print("Are new_list and my_list the same object?:", my_list is new_list)

print(id(my_list))
print(id(new_list))

# Modify an immutable element
my_list[0] = 100
print("My List:", my_list)
print("New List:", new_list)

# Modify a mutable element
my_list[3][0] = 300
print("My List:", my_list)
print("New List:", new_list)