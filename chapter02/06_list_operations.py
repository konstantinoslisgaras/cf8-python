# Populate a list within initial values (fruits):
fruits = ["Mango", "Peach", "Apricot", "Melon", "Pineapple"]
print("Initial list of fruits:", fruits)

# Add a single element at the end of the list:
fruits.append("Fig")
print("After adding 'Fig' in list of fruits:", fruits)

# Add multiple elements at the end of the list:
fruits.extend(["Watermelon", "Pear", "Papaya", "Coconut"])
print("After adding a new list of fruits:", fruits)

# Add a single element at a specific index of the list:
fruits.insert(1, "Grapes")
print("After adding 'Grapes' in position 1 in the list of fruits:", fruits)

# Update an element in the list:
fruits[0] = "Banana"
print("After updating the 0 index in the list of fruits:", fruits)

print(fruits[1:3])

# Update a slice in the list:
fruits[1:3] = ["Apple"]
print("After updating with slicing:", fruits)

# Delete with slice in the list:
fruits[3:6] = []
print("After deleting with slicing:", fruits)

# Delete an element by positioning with pop():
removed_item = fruits.pop(-2) # default is -1
print(f"Removed item: {removed_item}")
print(fruits)

# Delete an element by value with remove():
fruits.remove("Pear")
print("After removing 'Pear':", fruits)

fruit_to_remove = input("Enter fruit to delete: ")
if fruit_to_remove in fruits:
    fruits.remove(fruit_to_remove)
    print(f"Removed fruit '{fruit_to_remove}' from list.")
else:
    print(f"'{fruit_to_remove}' not in list.")

# Search for element in a list and get its' index position:
position = fruits.index("Watermelon")
print(f"Watermelon in position: {position}")