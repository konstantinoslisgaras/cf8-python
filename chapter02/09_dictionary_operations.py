products = {1: "Table", 2: "Chairs", 3: "Sofa", 10: "Bed"}

print(f"Initial products: {products}")

# Insert a new item:
products[11] = "Wardrobe"
print(f"After inserting a new pair: {products}")

# Access element by key:
products_1 = products.get(100, "product_not_found")
print(products_1)

# Delete:
del products[2]
print(f"After deleting: {products}")

# Remove item:
key, value = products.popitem()
print(key, ":", value)

removed_product = products.pop(3)
print(removed_product)
print(f"After popping: {products}")

key_to_find = 2
if key_to_find in products:
    print(f"Key {key_to_find} exists in products.")
else:
    print(f"Key {key_to_find} does not exist in products.")

# Iterate dictionary keys
for item in products.keys(): # for item in products:
    print(item, end=" ")
print()

# Iterate dictionary keys, values with indexing:
for key in products.keys(): # for item in products:
    print(f"Key: {key}, Value: {products[key]}")

# Iterate dictionary values
for value in products.values():
    print(value, end=" ")
print()

# Iterate key, value
for key, value in products.items():
    print(f"{key} : {value}")

print(products.items())
# Tuple unpacking
# [
# (1, 'Table'),
# (10, 'Bed')
# ]
