my_ints = [1, 2, 3, 4, 5]

my_dict = { num: num ** 2 for num in my_ints}

for key, value in my_dict.items():
    print(f"{key}:{value}")

print("="*30)

new_list = [value for key, value in my_dict.items() if value % 2 == 0]

print(f"List from dict:{new_list}")