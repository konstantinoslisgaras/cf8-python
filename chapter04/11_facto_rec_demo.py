def factorial(n: int) -> int:
    if n < 0:
        return 0
    if n in (0, 1): return n
    return n * factorial(n - 1)

def main():
    print(factorial(20))
    print(factorial(15))
    print(factorial(10))
    print(factorial(5))

if __name__ == "__main__":
    main()