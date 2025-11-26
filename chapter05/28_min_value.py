def main():
    students = { "Alma": 50, "Reina": 30, "Alpha": 80, "Kappa": 85 }

    student_with_lowest_grade = min(students, key=students.get)

    print(f"Student with the lowest grade is: {student_with_lowest_grade} with grade: {students[student_with_lowest_grade]}")

    print(f"Student with the smallest (alphabetically) name is: {min(students)}")
    
    print(f"Student with the shortest name is: {min(students, key=len)} with length: {len(min(students, key=len))}")

if __name__ == "__main__":
    main()