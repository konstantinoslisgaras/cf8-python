import logging

def logger_decorator(func):
    """
    Decorator to log the execution of a function.

    Params:
        func (function): The function to be decorated.

    Returns:
        (None): Creates a log file when the function is executed.
    """
    def inner_function(*args, **kwargs):
        """
        Wrapper function to create the log file of the decorated function.
        """
        log_file = 'func.log'
        file_handler = logging.FileHandler(log_file, mode='a')
        handlers = [file_handler]
        logger = logging.getLogger('log-decorator-app')

        logging.basicConfig(
            handlers=handlers,
            level=logging.INFO,
            format="%(asctime)s:%(levelname)s:%(name)s:%(message)s"
        )
        logger.info(f"{func.__name__}, was succesfully executed.")
        print(f"{func.__name__} logged succesfully")
        return func(*args, **kwargs)
    
    return inner_function

@logger_decorator
def add(a, b):
    return a + b

@logger_decorator
def sub(a, b):
    return a - b

def main():
    add(9, 5)
    sub(17, 3)

if __name__ == "__main__":
    main()