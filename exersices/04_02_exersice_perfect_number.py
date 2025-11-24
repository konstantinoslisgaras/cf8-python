def perfect_number_checker(num: int) -> bool:
    divisors = []

    for i in range(1, (num//2) + 1):
        if num % i == 0:
            divisors.append(i)

    total = sum(divisors)

    return total == num

def user_input_prompt() -> str:
    return input("Please enter an integer (max 5-digits): ")

def is_valid(num) -> bool:
    return num.isnumeric() and len(num) <= 5

def main():
    while True:
        try:
            num = user_input_prompt()
            if is_valid(num):
                print(perfect_number_checker(int(num)))
        except ValueError:
            continue

if __name__ == "__main__":
    main()