import time

def log_calls(func):
    """A decorator that logs the function call."""
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__} with arguments: {args} and kwargs: {kwargs}")
        return func(*args, **kwargs)
    return wrapper

def measure_time(func):
    """A decorator that measure the execution time of the function."""
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter_ns()
        result = func(*args, **kwargs)
        end_time = time.perf_counter_ns()
        print(f"Execution time of function: {func.__name__} is {end_time - start_time:.6f} ns")
        return result
    return wrapper

@log_calls
@measure_time
def say_hello(name):
    return f"Hello {name}!"

def main():
    print(say_hello("Kappa"))

if __name__ == "__main__":
    main()