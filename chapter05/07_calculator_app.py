import functools

def calculate(args):
    def plus():
        return functools.reduce(lambda x, y: x + y, args)

    def minus():
        return functools.reduce(lambda x, y: x - y, args)
        
    def mul():
        return functools.reduce(lambda x, y: x * y, args)

    return {
        "add": plus,
        "subtract": minus,
        "multiply": mul
    }

def main():
    ints_list = [14, 34, 80, 7, 50]
    operations = calculate(ints_list)

    while True:
        print("\nChoose an operation")
        print("1. Addition")
        print("1. Subtraction")
        print("3. Multiplication")
        print("4. Exit")

        try:
            choice = int(input("Please enter your choice (1-4): "))
        except ValueError:
            print("Invalid input.")
            continue

        match choice:
            case 1:
                print("Addition result:", operations['add']())
            case 2:
                print("Subtraction result:", operations['subtract']())
            case 3:
                print("Multiplication result:", operations['multiply']())
            case 4:
                print("Exiting...")
                break
            case _:
                print("Invalid choice. Please try again.")
                       
if __name__ == "__main__":
    main()