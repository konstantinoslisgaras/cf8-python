class Student:
    """
    A class that represents a student with a firstname and a lastname.

    Attributes:
        firstname (str): The firstname of the student.
        lastname (str): The lastname of the student.
    """
    def __init__(self, firstname: str, lastname: str):
        self._firstname = firstname
        self.lastname = lastname

def main():
    athina = Student("Alpha", "Alpha")
    student = Student("Kappa", "Lambda")
    print("Firstname:", student.firstname)
    print("Lastname:", student.lastname)
    print("Firstname:", athina.firstname)
    print("Lastname:", athina.lastname)

if __name__ == "__main__":
    main()