def calculate_sum_and_product(upper_bound: int):
    total_sum = 0
    total_product = 1

    for i in range(1, upper_bound + 1):
        total_sum += i
        total_product *= i

    return total_sum, total_product

def main():
    try:
        upper_bound = int(input("Please enter a positive integer: "))
        if upper_bound <= 0:
            raise ValueError
    except ValueError:
        print("Invalid input.")
        return
    
    total_sum, total_product = calculate_sum_and_product(upper_bound)

    print(f"Total sum from 1 to {upper_bound} = {total_sum}")
    print(f"Total product from 1 to {upper_bound} = {total_product}")

if __name__ == "__main__":
    main()