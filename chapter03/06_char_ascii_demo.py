def process_characters_1() -> None:
    """
    Reads characters from the user and prints the ASCII characters until user inputs '#'.
    """

    ch = input("Please insert a character: ")

    while ch != '#':
        print(ch, ":", ord(ch))
        ch = input("Please insert a character: ")
    else:
        print("You cracked the code!")

    print("Goodbye!")

def process_characters_2() -> None:
    """
    Reads characters from the user and prints the ASCII characters until user inputs '#'.
    """

    while True:
        ch = input("Please insert a character: ")
        if ch == '#':
            break
        else:
            print(ch, ":", ord(ch))

    print("Goodbye!")

def main():
    process_characters_1()

if __name__ == "__main__":
    main()