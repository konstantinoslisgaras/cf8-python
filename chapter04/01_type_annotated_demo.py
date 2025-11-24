def my_add(a: int | float, b: int | float) -> int | float:
    """
    Add two numbers and returns the result.

    Args:
        a (int, float): The first number to add. 
        b (int, float): The second number to add.

    Returns:
        int | float: The sum of a + b

    Raises:
        TypeError: If either a or b is not integer or float.
    """
    if not (isinstance(a, (int, float))) or (isinstance(b, (int, float))):
        raise TypeError("The numbers must be integers of floats.")
    return a + b

def main():
    try:
        result = my_add("hello", "world")
        print(result)
    except TypeError as e:
        print(e)

    # 1. Annotations.
    print("Annotations:", my_add.__annotations__)

    # 2. Doc comments
    print("Docs:", my_add.__doc__)      

if __name__ == "__main__":
    main()