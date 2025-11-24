def fahrenheit_to_celsius(temp: float) -> float:
    return round((temp - 32) * 5/9, 2)

def main():
    fahrenheit_temps = [31, 67, 90, 102, 75, 68, 55]

    # List comprehension
    celsius_temp_list = [fahrenheit_to_celsius(temp) for temp in fahrenheit_temps]
    print("Celsius temperatures:", celsius_temp_list)
    print(type(celsius_temp_list))

    #
    celsius_temps = [fahrenheit_to_celsius(temp) for temp in fahrenheit_temps]
    print("Celsius temperatures:", celsius_temps)
    for celsius in celsius_temps:
        print(celsius, end=" ")
    print()

    for celsius in celsius_temps:
        print(celsius, end=" ")
    print()

if __name__ == "__main__":
    main()