def print_id(variable_name, variable):
    print(f"id({variable_name}) = {id(variable)}")

def main():
    original_list = [1, 2, 3]

    new_list = original_list

    print_id("OG", original_list)
    print_id("NL", new_list)

    print(f"OG is NL: {original_list is new_list}")

    temp_list = [1, 2, 3]
    print_id("TL", temp_list)
    print(f"OG is TL: {original_list is temp_list}")

if __name__ == "__main__":
    main()