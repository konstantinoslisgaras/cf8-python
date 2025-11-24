def test_args_func(pos_args_1, pos_args_2, opt_arg_1=None, opt_arg_2=None, *args, **kwargs):
    """
    Function to demonstrate the usage of positional, optional, additional position and additional keyword arguments.

    Params:
        pos_args_1 (Any): The first positional argument.
        pos_args_2 (Any): The second positional argument.
        opt_arg_1: The first optional argument. Defaults to None.
        opt_arg_2: The second optional argument. Defaults to None.
        *args (tuple): Additional positional arguments.
        **kwargs (dict): Additional keyword arguments.
    """
    # Printing positional arguments
    print("Pos arg 1", pos_args_1)
    print("Pos arg 2", pos_args_2)

    # Printing optional arguments
    print("Opt arg 1", opt_arg_1)
    print("Opt arg 2", opt_arg_2)

    # Printing additional positional arguments
    if args:
        print("Additional Positional Arguments")
        for arg in args:
            print(arg)

    # Printing additional keyword arguments
    if kwargs:
        print("Additional Keyword Arguments")
        for key, value in kwargs.items():
            print(f"{key}:{value}")

def main():
    test_args_func("Kappa", "Lambda", opt_arg_1=14, opt_arg_2=34)
    print("="*50)
    test_args_func("Kappa", "Lambda", opt_arg_1=14, opt_arg_2=34, keyw_args_1="Python", keyw_args_2="Android")
    print("="*50)
    test_args_func(
        "K", "L",        # pos_arg_1, pos_arg_2
        100, 200,        # opt_arg_1, opt_arg_2
        500, 800,        # *args
        p="Python", a="Android" # **kwargs
    )

if __name__ == "__main__":
    main()