def add(a: int, b: int, c: int = 0) -> int:
    """
    Calculate the sum of two or three integers.

    Parameters:
        a (int): The first number to add.
        b (int): The second number to add.
        c (int, optional): The third number to add, defaults to 0 if not provided.

    Returns:
        int: The sum of the provided numbers.
    """
    return a + b + c

def full_opt_add(a: int = 0, b: int = 0, c: int = 0) -> int:
    return a + b + c

def main():
    print(add(10, 40))
    print(full_opt_add())

if __name__ == "__main__":
    main()