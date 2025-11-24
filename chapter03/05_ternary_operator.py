def compare_integers(a: int, b: int) -> None:
    """
    Compares two integers and prints the result.

    Args:
        a (int): The first integer to compare.
        b (int): The second integer to compare.

    Returns:
        None.
    """
    if a == b:
        print("Numbers are equal.")
    elif a > b:
        print("First number is greater than second number.")
    else:
        print("Second number is greater than first number.")

def main():
    try:
        a = int(input("Please enter the first number: "))
        b = int(input("Please enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter valid integers.")
        return
    
    compare_integers(a, b)

    # 1. Ternary operator (simple)
    # 'Positive', 'Non positive'
    result = "Positive" if a >= 0 else "Negative"
    print(result)

    # 2. Ternary operator (extended)
    result = (
        "The numbers are equal" if a == b else
        "The first number is greater than the second number" if a > b else
        "The second number is greater than the first number"
    )
    print(result)

if __name__ == "__main__":
    main()