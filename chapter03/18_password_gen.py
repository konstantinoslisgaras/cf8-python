import string
import random

# ASCII letters, digits, !@#$%^&*

characters = list(string.ascii_letters + string.digits + "!@#$%^&*")

def generate_password():
    try:
        password_length = int(input("Password length?: "))
        if password_length < 5:
            password_length = 5
    except ValueError:
        print("Invalid input.")
        return
    
    random.shuffle(characters)
    password = []
    for i in range(password_length):
        password.append(random.choice(characters))

    random.shuffle(password)
    password = "".join(password)

    print(f"\nGenerated password: {password}")

def main():
    while True:
        option = input("Do you want to create a password? (y/n) ")
        if option.lower() == 'y':
            generate_password()
        else:
            print("Exiting...")
            break

if __name__ == "__main__":
    main()