def main():
    num = int(input("Please enter an integer: "))

    # Initialize the first two fibonacci numbers
    a = 0
    b = 1

    for i in range(2, num + 1):
        temp = a
        a = b
        b = temp + b

    print(f"The {num} Fibonacci is {b}")

if __name__ == "__main__":
    main()