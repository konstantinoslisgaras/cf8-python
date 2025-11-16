def print_cities(*cities):
    # Check if any city was provided
    if not cities:
        print("No cities provided.")
    else:
        print("Cities:", ", ".join(cities))


def main():
    print_cities("Mexico City", "Athens", "Barcelona")
    print_cities()
    print_cities("Vienna")

if __name__ == "__main__":
    main()