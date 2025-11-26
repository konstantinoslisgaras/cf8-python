from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n):
    if n <= 1: return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def fibo_with_logging(n):
    if fibonacci.cache_info().hits > 0:
        print(f"Cache hit for fibonacci({n}).")
    else:
        print(f"Calculating fibonacci({n}).")
    return fibonacci(n)

def main():
    # print([fibonacci(n) for n in range(10)])
    fibonacci.cache_clear()

    fibo_nums = [fibo_with_logging(n) for n in range(10)]
    print(fibo_nums)

if __name__ == "__main__":
    main()