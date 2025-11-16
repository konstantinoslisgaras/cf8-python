def get_average(*numbers):
    if not numbers:
        return "No numbers provided."
    
    average = sum(numbers) / len(numbers)
    return "{0:.2f}".format(average)

def main():
    numbers = [10, 15, 20]
    print(get_average(*numbers)) # Unpacking
    print(get_average(100, 200, 300)) # Unpacking

if __name__ == "__main__":
    main()