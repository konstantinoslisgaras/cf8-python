import random

def get_user_guess():
    while True:
        try:
            return int(input("Please insert an integer: "))
        except ValueError:
            print("Invalid input!", end=" ")
            continue

def check_guess(secret: int, guess: int):
    if guess == secret:
        print("Bingo! Secret number was", secret)
        return True
    elif abs(guess - secret) <= 5:
        print("HOT!!!")
    else:
        print("cold...")
    return False

def main():
    secret_number = random.randint(1, 100)
    MAX_TRIES = 15
    try_count = 0

    while try_count < MAX_TRIES:
        guess = get_user_guess()
        if check_guess(secret_number, guess):
            break
        else:
            try_count += 1

    if try_count == MAX_TRIES:
        print("Reached max try count...")
        print("Secret number was:", secret_number)

if __name__ == "__main__":
    main()