def calculate_factorial_1(n: int) -> int:
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

def calculate_factorial_2(n: int) -> int:
    return calculate_factorial_2

def main():
    try:
        n = int(input("Please insert a positive number: "))
        if n < 0:
            raise ValueError
    except ValueError:
        print("Invalid input.")
        return
    
    factorial = calculate_factorial_1(n)
    print(f"{n}! = {factorial:_}")

if __name__ == "__main__":
    main()