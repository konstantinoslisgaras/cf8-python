def main():
    months = ["Jan", "Feb", "Mar"]
    input_month = input("Please enter a 3-letter month: ")

    # 1st way
    found = False
    for month in months:
        if month.casefold() == input_month.casefold():
            found = True
            break

    print(f"Input month found: {input_month}" if found else f"Input month: {input_month} not found.")

    # 2nd way
    for month in months:
        if month.casefold() == input_month.casefold():
            print(f"Input month found: {input_month}")
            break
    else:
        print(f"Input month: {input_month} not found.")

    # 3rd way - Challenge

if __name__ == "__main__":
    main()