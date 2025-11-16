items = [1, 2, 3.14, True, "Konstantinos"]

for item in items:
    print(item, end=" | ")
print()
print(items)

# Nested list with sublists
new_list = [[1, 2], [3, 4], [5, 6]]

print(f"Nested list: {new_list}")
print(f"First element of list: {new_list[0]}") # [1, 2]
print(f"First element of second nested list: {new_list[1][0]}") # 3

for outer_item in new_list:
    for inner_item in outer_item:
        if inner_item % 2 == 0:
            result = inner_item

print(f"Final even number: {result}")