def enroll_stundents(*students, min_grade=50, department="Computer Science", **kwargs):
    """
    Enroll student in a department with a minumum grade requirement and some additional information.

    Params:
        *students (str): Name of students that enrolled.
        min_grade (int, optional): Minimum grade required to enroll. Defaults to 50.
        department (str, optional): Department for enrollment. Defaults to 'Computer Science'.
        **kwargs (dict): Additional keywords arguments for extra information. 
    """
    print("Minimum grade:", min_grade)
    print("Department:", department)

    print("\nEnrolled Student")
    for student in students:
        print(f" - {student}")

    print("\nAdditional Information")
    for key, value in kwargs.items():
        print(f"{key} : {value}")

    print("=== End of Enrollment ===\n")

def main():
    enroll_stundents("Kappa", "Lambda")
    enroll_stundents("Alpha", "Alpha", academic_year=2025, semester="Spring")
    enroll_stundents("Reina", "Alma", min_grade=70, department="Animals", academic_year=2025, semester="Spring")

if __name__ == "__main__":
    main()