def fibo():
    """
    Generator function to yield numbers in the Fibonacci sequence indefinitly.

    Yields:
        int: The next number in the Fibonacci sequence.
    """
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def main():
    fib = fibo()

    for i in range(10):
        print(f"Fib ({i}) = {next(fib)}")

    fib2 = fibo()

    fib_list = [next(fib2) for _ in range(10)]
    print(fib_list)

if __name__ == "__main__":
    main()