def print_cities(*cities, sep=", ", end="\n"):
    """
    Prints a list of cities separated by a specified separator and ends with a specified end character.

    Params:
        *cities (str): A variable number of city names to be printed.
        sep (str): Separator between city names. Default is ", ".
        end (str): End character after the last city. Default is "\n".
    """

    if not cities:
        print("No cities provided.", end=end)
    else:
        print("Cities:", sep.join(cities), end=end)

def main():
    print_cities("Mexico City", "Oaxaca", "Palenque")
    print_cities("Cancun")
    print_cities("Merida", "Chichen Itza", sep="-", end="*\n")

if __name__ == "__main__":
    main()