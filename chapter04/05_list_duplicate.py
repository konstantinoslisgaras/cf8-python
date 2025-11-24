my_list = [1, 2, "Hello", [3, 4, 5]]

print("At the start")
for item in my_list:
    print(f"{item} : {id(item)}")

# Duplicate list
new_list = my_list * 2
print("Duplicated List:", new_list)

# 1. Modify the first element
new_list[0] = 100
print("My list:", my_list)
print("New list:", new_list)

# 2. Modify and element of the nested list
new_list[3][0] = 300 
print("My list:", my_list)
print("New list:", new_list)

print("At the end")
for item in new_list:
    print(f"{item} : {id(item)}")