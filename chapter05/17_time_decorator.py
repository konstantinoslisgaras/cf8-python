import time

def timer_decorator(func):
    """
    Decorator to measure the execution time of a function.

    Params:
        func (function): The function to be decorated.

    Returns:
        function: The decorated function with added timing functionality.
    """
    def inner_function(*args, **kwargs):
        """
        Wrapper function to calculate the execution time of the decorated function.
        """
        start_time = time.time()            # Records start time.
        result = func(*args, **kwargs)      # Execution of the decorated function.
        end_time = time.time()              # Records end time.
        print(f"{func.__name__} took {end_time - start_time} seconds to run")
        return result                       # The result of the decorated function.
    
    return inner_function

@timer_decorator
def sum_function(num):
    return sum(range(num + 1))

print(sum_function(1_000_000))

@timer_decorator
def reverse_string(s: str) -> str:
    return "".join(reversed(s))

print(reverse_string("Kappa Lambda"))

if __name__ == "__main__":
    pass