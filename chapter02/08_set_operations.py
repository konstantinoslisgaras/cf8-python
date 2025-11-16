# Set of items in a bag:
bag = {"Power bank", "Wallet", "Tissues", "Smartphone", "Bottle", "Tissues"}

print("Initial Set:", bag)

# Add a new item:
bag.add("Book")
bag.add("Book")
bag.add("Book")
print("After adding book:", bag)

# Remove an item:
item_to_remove = "Tissues"
bag.remove(item_to_remove)
print("After removing:", item_to_remove, bag)

if item_to_remove in bag:
    bag.remove(item_to_remove)
    print(item_to_remove, "removed")
else:
    print(item_to_remove, "was not removed")

# Iterate through set
for item in bag:
    print(item, end="|")
print()