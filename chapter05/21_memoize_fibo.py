def memoize(func):
    """
    A simple memoization decoration to cache the results of the function.
    """
    cache = {}
    cache_stats = {
        "hits": 0,
        "misses": 0
    }
    def wrapper(n):
        if n in cache:
            print(f"Cache hit for Fibonacci {n}.")
            cache_stats["hits"] += 1
        else:
            print(f"Calculating Fibonacci {n}.")
            cache[n] = func(n)
            cache_stats["misses"] += 1
        return cache[n]
    
    wrapper.cache_stats = cache_stats
    return wrapper

@memoize
def fibonacci(n):
    if n <= 1: return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def main():
    print([fibonacci(n) for n in range(10)])
    print(fibonacci.cache_stats)

if __name__ == "__main__":
    main()