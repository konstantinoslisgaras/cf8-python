def facto():
    """
    Generator function to yield factorials indefinitly.

    Yields:
        int: The next factorial in the sequence.
    """
    n, result = 0, 1
    while True:
        yield result
        n += 1
        result *= n

def main():
    f = facto()

    for i in range(6):
        print(f"{i}! = {next(f)}")

    print(f"6! = {next(f)}")
    
    for i in range(7, 11):
        print(f"{i}! = {next(f)}")

if __name__ == "__main__":
    main()