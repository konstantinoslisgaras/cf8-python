def calculator(n1: int, n2: int, operation):
    """
    A calculator function that applies a passed operation (function) in two integers.

    Args:
        n1 (int): The first number.
        n2 (int): The second number.
        operation (function): A function that takes two integers and returns an integer.

    Returns:
        int: The result of applying the operation function to n1 and n2.
    """

    try:
        return operation(n1, n2)
    except TypeError as e:
        print(f"Error: {e}. Ensure the operation is supported.")
    
def add(no1, no2):
    return no1 + no2

def subtract(no1, no2):
    return no1 - no2

def multiply(no1, no2):
    return no1 * no2

def divide(no1, no2):
    if no2 == 0:
        raise ValueError("Division by zero is not allowed.")
    return no1 / no2

def kappa_addition(a, b, c):
    return a + b + c

def main():
    print("Addition:", calculator(5, 3, add))
    print("Subtraction:", calculator(5, 3, subtract))
    print("Multiplication:", calculator(5, 3, multiply))
    print("Addition:", calculator(5, 3, add))
    print("Kappa_Addition:", calculator(5, 3, kappa_addition))

if __name__ == "__main__":
    main()