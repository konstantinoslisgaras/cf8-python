def main():
    grades = [7, 5, 9, 10, 3]

    # List comprehension
    upscaled_grades_1 = [grade + 1 if grade <= 9 else grade for grade in grades]
    print("Upscaled grades 1:", upscaled_grades_1)

    # Using map
    upscaled_grades_2 = list(map(lambda grade: grade + 1 if grade <= 9 else grade, grades))
    print("Upscaled grades 2:", upscaled_grades_2)

    # Filtering with list comprehension
    passed_grades_1 = [grade for grade in grades if grade >= 5]
    print("Passed grades 1:", passed_grades_1)

    # Filtering with lambda
    passed_grades_2 = list(filter(lambda grade: grade >= 5, grades))
    print("Passed grades 2:", passed_grades_2)
    
if __name__ == "__main__":
    main()