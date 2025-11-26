from functools import reduce

def main():
    months = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]
    
    sales = [12_000, 14_000, 13_200, 15_000, 20_000, 18_500,
             16_000, 15_500, 14_000, 19_000, 22_500, 24_000]
    
    # Create a dictionary (key = months, value = sales)
    monthly_sales = dict(zip(months, sales))
    print(monthly_sales)

    # Apply a 10% discount for sales above 20_000
    discounted_sales = {
        month: value * 0.9 if value > 20_000 else value for month, value in monthly_sales.items()
    }
    print(discounted_sales)

    best_month = max(monthly_sales, key=monthly_sales.get)
    worst_month = min(monthly_sales, key=monthly_sales.get)

    print(f"Best month for my sales was: {best_month} and worst was: {worst_month}")

if __name__ == "__main__":
    main()