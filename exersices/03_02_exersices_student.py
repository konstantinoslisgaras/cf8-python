from datetime import datetime
import random

class Student:
    __students_counter = 0

    def __init__(self, firstname: str, lastname: str, year_of_birth: int, lessons: list[str]):
        Student.__students_counter += 1
        self.__id = Student.id_generator()
        self._firstname = firstname
        self._lastname = lastname
        self._year_of_birth = year_of_birth
        self.lessons = lessons
        self.__age = Student.age_calculator(year_of_birth)

    @classmethod
    def id_generator(cls):
        return f"{cls.__students_counter}-{random.randint(1000, 9999)}"
    
    @staticmethod
    def age_calculator(year_of_birth):
        return (datetime.now().year - year_of_birth)

    def __str__(self):
        return f"ID: {self.__id}\n{self._lastname} {self._firstname}\nAge: {self.age} | Born: {self._year_of_birth}\nNumber of Lessons: {len(self.lessons)}"

    def print_lessons(self):
        for key, value in enumerate(self.lessons, start=1):
            print(f"{key}: {value}", sep="|", end = " ")
            print()
    
    @classmethod
    def get_count(cls):
        return Student.__students_counter
    
    @property
    def id(self):
        return self.__id
    
    @property
    def firstname(self):
        return self._firstname
    
    @firstname.setter
    def firstname(self, firstname):
        self._firstname = firstname

    @property
    def lastname(self):
        return self._lastname
    
    @lastname.setter
    def lastname(self, lastname):
        self._lastname = lastname

    @property
    def year_of_birth(self):
        return self._year_of_birth
    
    @year_of_birth.setter
    def year_of_birth(self, year_of_birth):
        self._year_of_birth = year_of_birth

    @property
    def age(self):
        return self.__age
    
    def add_lesson(self, lesson):
        self.lessons.append(lesson)
        print(f"Lesson {lesson} added.")

    def remove_lesson(self, lesson):
        if lesson not in self.lessons:
            print("Lesson not in student's list.")
            return
        else:
            self.lessons.remove(lesson)
            print(f"Lesson {lesson} removed.")
    

def main():
    kappa = Student(
        "Kappa",
        "Lambda",
        1991,
        ["Python", "Java", "React", "Databases"]
    )
    kappa.add_lesson("GoLang")
    kappa.remove_lesson("React")

    alpha = Student(
        "Alpha",
        "Alpha",
        1991,
        ["C#", "JavaScript"]
    )

    print(kappa)
    kappa.print_lessons()
    print(alpha)

if __name__ == "__main__":
    main()