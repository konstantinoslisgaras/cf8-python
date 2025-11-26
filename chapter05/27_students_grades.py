students = {
    "Alma": [85, 90, 70],
    "Reina": [55, 80, 100],
    "Alpha": [60, 90, 100],
    "Kappa": [90, 100, 95]
}

def main():
    while True:
        try:
            threshold = int(input("Please insert the threshold: "))
            break
        except ValueError:
            print("Invalid input. Try again.")

    average_grade = {
        student: round(sum(grades) / len(grades), 2)
        for student, grades in students.items()
        if grades and (sum(grades) / len(grades)) > threshold
    }

    print(average_grade)

if __name__ == "__main__":
    main()