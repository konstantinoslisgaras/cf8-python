import time

def get_time(n: int) -> int:
    start_time = time.time()

    result = sum(range(n + 1))

    end_time = time.time()

    print(f"Total time passed: {end_time - start_time:.5f} | {n} = {result}")

def main():
    get_time(10)
    get_time(100_000_000)
    get_time(500_000_000)

if __name__ == "__main__":
    main()