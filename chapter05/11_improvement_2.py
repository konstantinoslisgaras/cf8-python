def upscale_grades(students_grades):
    """
    Upscale grades by adding 1 to each grades less than or equal to 9.
    """
    return {name: (grade + 1 if grade <= 9 else grade) for name, grade in students_grades.items()}

def filter_passed(students_grades):
    return {name: grade for name, grade in students_grades.items() if grade >= 5}

def categorize_grades(students_grades):
    passed = {name: grade for name, grade in students_grades.items() if 5 <= grade < 10}
    failed = {name: grade for name, grade in students_grades.items() if grade < 5}
    honored = {name: grade for name, grade in students_grades.items() if grade == 10}
    return passed, failed, honored

def calculate_average(students_grades):
    if students_grades:
        return sum(students_grades.values()) / len(students_grades)
    else:
        return 0

def main():
    students_grades = {
        "Alpha": 10,
        "Kappa": 8,
        "Alma": 5,
        "Reina": 2,
        "Nellie": 7,
        "Oliver": 10
    }

    upscale = upscale_grades(students_grades)
    print(upscale)

    passed, failed, honored = categorize_grades(students_grades)
    print("\nPassed students")
    for name, grade in passed.items():
        print(f"{name} - {grade}")

    print("\nFailed students")
    for name, grade in failed.items():
        print(f"{name} - {grade}")

    print("\nHonored students")
    for name, grade in honored.items():
        print(f"{name} - {grade}")

if __name__ == "__main__":
    main()