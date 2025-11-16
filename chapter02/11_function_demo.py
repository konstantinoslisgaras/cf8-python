# imports
# definitions
# def main()

def say_hello(name: str = "User") -> None:
    """
    Prints a greeting message.

    Args:
        name (str): The name to greet. Defaults to 'User'.
    """
    print(f"Hello {name}!")

def main():
    say_hello("Konstantinos")
    say_hello(5)
    say_hello()
    print(say_hello.__doc__)

if __name__ == "__main__":
    # Execute main function if the script is run directly.
    main()