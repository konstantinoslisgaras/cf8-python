import re

stack = [] # empty stack
num = 0    # variable to store

# Push an item onto the stack
def push(list, item):
    list.append(item)

def pop(list):
    if list:
        return list.pop()
    else:
        print("Stack is Empty.")

def print_stack(list):
    if list:
        print("Current stack:", list)
    else:
        print("Stack is empty")

def print_menu():
    print("1. Insert on top")
    print("2. Get from top")
    print("3. Print current state")
    print("4. q/Q to Quit")

def get_choice():
    return input("Please enter your choice: ")

def main():
    choice = 0
    num = 0
    out_num = 0

    while (True):
        print_menu()
        choice = get_choice()

        if not choice:
            continue

        if choice == "q" or choice == "Q":
            break

        # r: Raw string literal.
        # ^: Asserts position at the start of the string.
        # \d: Matches any digit (0-9)
        # \d+: Matches any digit (0-9). 1 or more.
        # $: Asserts position at the end of the string.
        pattern = r"^\d$"

        valid = re.match(pattern, choice)

        if not valid:
            print("Error in choice")
            continue

        choice = int(choice)

        match choice:
            case 1:
                num = input("Please enter a number: ")
                pattern_push = r"^\d+$"
                valid = re.match(pattern_push, num)

                if not valid:
                    print("Error...")
                    continue

                num = int(num)
                push(stack, num)
                print(str(num) + " inserted.")

            case 2:
                out_num = pop(stack)

                if out_num is not None:
                    print("You got", out_num)

            case 3:
                print_stack(stack)

            case 4:
                break
            
            # default case
            case _:
                print("Not a valid choice.")

if __name__ == "__main__":
    main()