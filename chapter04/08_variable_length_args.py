def my_add(*args: int) -> int:
    return sum(args)

def my_avg(*args: int) -> int | float:
    if not args:
        return 0
    return sum(args) / len(args)

def main():
    ages = [10, 34, 41, 65, 21]
    print("Average:", my_avg(*ages))
    print("Average:", my_avg(10, 34, 41, 65, 21))
    print("Average of an empty list:", my_avg())

if __name__ == "__main__":
    main()