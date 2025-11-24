def user_input_prompt() -> str:
    return input("Please enter an integer (max 8-digits): ")

def is_valid(num) -> bool:
    return num.isnumeric() and len(num) <= 8

def is_armstrong(num) -> str:

    length = len(str(num))
    total_digit_sum = 0
    for digit in num:
        total_digit_sum += int(digit) ** length

    return f"{num} IS an Armstrong number." if int(num) == total_digit_sum else f"{num} IS NOT an Armstrong number."

def main():
    while True:
        try:
            num = user_input_prompt()
            if is_valid(num):
                print(is_armstrong(num))
            else:
                continue
        except ValueError:
            continue
       
if __name__ == "__main__":
    main()