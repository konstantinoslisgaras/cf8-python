def name_spacing(num):
    if not isinstance(num, int):
        print("The number of spaces must be an integer.")
        return
    
    if num < 0:
        print("The number of spaces must be a positive integer.")
        return
    
    name = input("Please insert a name: ").strip()

    if not name:
        print("No name provided.")
        return
    
    spaced_name = (" " * num).join(name)
    print(spaced_name)

def main():
    name_spacing(5)

if __name__ == "__main__":
    main()