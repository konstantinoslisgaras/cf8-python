def get_formatted_date(day: int = 1, month: int = 1, year: int = 2000) -> str:
    """
    Returns a string representation of a date in the format "dd/mm/yyyy"

    Args:
        day (int): The day of the month. Defaults to 1.
        month (int): The month of the year. Defaults to 1.
        year (int): The year of the date. Defaults to 2000.

    Returns:
        str: The formatted date string.
    """
    return(f"{day:02d}/{month:02d}/{year:4d}")

def main():
    print(get_formatted_date())
    print(get_formatted_date(10))
    print(get_formatted_date(10, 10))
    print(get_formatted_date(14, 11, 1991))
    print(get_formatted_date(year=2025))
    print(get_formatted_date.__doc__)

if __name__ == "__main__":
    main()