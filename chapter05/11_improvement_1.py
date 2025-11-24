def upscale_grades(grades):
    upscaled = [grade + 1 if grade <= 9 else grade for grade in grades]
    return upscaled

def filter_passed_grades(grades):
    passed = [grade for grade in grades if grade >= 5]
    return passed

def categorize_grades(grades):
    passed = [grade for grade in grades if grade >= 5 and grade < 10]
    failed = [grade for grade in grades if grade < 5]
    honors = [grade for grade in grades if grade == 10]

    return passed, failed, honors

def calculate_average(grades):
    return sum(grades) / len(grades) if grades else 0
    
def main():
    grades = [7, 5, 10, 3, 4, 8, 10, 9, 2, 7, 6, 10]

    print("Upscaled grades:", upscale_grades(grades))
    print("Passed grades:", filter_passed_grades(grades))

    passed, failed, honors = categorize_grades(grades)
    print("Passed:", passed)
    print("Failed:", failed)
    print("Honored:", honors)

    print("Averaged grades:", calculate_average(grades))
    
if __name__ == "__main__":
    main()