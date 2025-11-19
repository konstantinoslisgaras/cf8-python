def is_square(length: float, width: float) -> bool:
    """
    Checks if a rectangle is square.

    Args:
        length (float): The length of the rectangle.
        width (float): The width of the rectangle.

    Returns:
        bool: True if the rectangle is square, false otherwise.

    """
    return length == width

def main():
    try:
        length = float(input("Please the length of the rectangle: "))
        width = float(input("Please the width of the rectangle: "))
    except ValueError:
        print("Invalid input.")
        return
    
    if is_square(length, width):
        print("Rectangle is a square.")
    else:
        print("Rectangle is not a square.")

if __name__ == "__main__":
    main()