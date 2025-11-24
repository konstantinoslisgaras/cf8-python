import re

def print_welcome_message() -> None:
    print("\n" + "="*10, "Welcome to my Queue app!!!", "="*10)

def print_menu() -> None:
    print("\n" + "Queue Options Menu")
    print("1. Add to queue.")
    print("2. Remove from queue.")
    print("3. Print queue.")
    print("4. Exit queue app.")

def user_choice_input() -> int:
    return input("Please enter your choice: ")

def user_queue_input() -> int:
    return input("Please enter a number (1 - 999) to add: ")

def is_valid(num) -> bool:
    pattern = r"^[1-9]\d{0,2}$"
    if re.match(pattern, num):
        return True
    else:
        return False

def insert(queue, num) -> None:
    queue.append(num)

# Option 1
def add_to_queue(queue, num) -> None:
    num = user_queue_input()
    while (True):
        if is_valid(num):
            insert(queue, int(num))
            print(f"Added number: | {num} |.")
            break
        else:
            print("Invalid number.")
            num = user_queue_input()
            continue

# Option 2
def remove_from_queue(queue) -> None:
    if not queue:
        print("The queue is empty. Try to add some numbers.")
    else:
        print(f"Removed number: | {queue.pop(0)} |.")

# Option 3
def print_queue(queue) -> None:
    print("Your queue")
    for i in range(len(queue)):
        print(f"{i + 1}: | {queue[i]:03d} |", end= " ")

# Option 4
def print_exit_message() -> None:
    print("\n" + "Thank for using my Queue app! Exiting...")

# Option default
def default_case(exit_choice) -> None:
    print(f"Invalid choice. Please enter an option 1 to {exit_choice - 1}. Enter {exit_choice} to exit the application.")

def main():
    queue = []
    choice = 0
    EXIT_CHOICE = 4
    num = 0

    print_welcome_message()

    while (choice != EXIT_CHOICE):
        print_menu()
        choice = int(user_choice_input())

        match choice:
            case 1:
                add_to_queue(queue, num)

            case 2:
                remove_from_queue(queue)

            case 3:
                print_queue(queue)

            case 4:
                print_exit_message()
            
            case _:
                default_case(EXIT_CHOICE)
                continue

if __name__ == "__main__":
    main()