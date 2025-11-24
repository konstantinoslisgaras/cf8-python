def is_armstrong_num(num: int) -> bool:
    """
    Checks if a number is an Armstrong number.

    Args:
        num (int): The number to check.

    Returns:
        bool: True if the number is an Armstrong number, False otherwise.
    """
    digits = str(num)
    power = len(digits)
    total = 0

    for digit in digits:
        total += int(digit) ** power

    return num == total

def main():
    try:
        num = int(input("Please enter an integer: "))
    except ValueError:
        print("Invalid input.")
        return
    
    if is_armstrong_num(num):
        print(f"{num} is an Armstrong number.")
    else:
        print(f"{num} is not an Armstrong number.")

if __name__ == "__main__":
    main()