from typing import List

class Person:
    def __init__(self, name: str, age: int):
        self._name = name
        self._age = age

    def get_name(self) -> str:
        return self._name

    def get_age(self) -> int:
        return self._age

    def study(self) -> None:
        print(f"{self._name} is studying.")

    def display_info(self) -> None:
        pass

class Student(Person):
    def __init__(self, name: str, age: int):
        super().__init__(name, age)
        self._student_id = None
        self._semester = None

    def get_student_id(self) -> str:
        return self._student_id

    def study(self) -> None:
        print(f"{self.get_name()} (Student) is studying in semester {self._semester}.")

    def study(self) -> None:
        print("Letsgoooooooooo")

    def display_info(self) -> None:
        print(f"Student ID: {self.get_student_id()}")
        print(f"Grades: {self.get_grades()}")
        print(f"Average Grade: {self.calculate_average()}")
        print(f"Rank: {self.calculate_rank()}")

    def take_exam(self) -> None:
        print(f"{self.get_name()} is taking an exam.")

class Teacher(Person):
    def __init__(self, name: str, age: int):
        super().__init__(name, age)
        self._employee_id = None
        self._class_name = None

    def get_employee_id(self) -> str:
        return self._employee_id

    def display_info(self) -> None:
        print(f"Employee ID: {self.get_employee_id()}")
        print(f"Class Name: {self._class_name}")

    def teach(self) -> None:
        print(f"{self.get_name()} is teaching a class.")

    def teach(self):
        print("Wegooooooo")

class Grades(Student):
    def __init__(self, name: str, age: int):
        super().__init__(name, age)
        self._daily_grade = 0
        self._exam_grade = 0
        self._quiz_grade = 0

    def get_grades(self) -> List[int]:
        return [self._daily_grade, self._exam_grade, self._quiz_grade]

    def study(self) -> None:
        self._daily_grade = int(input("Enter daily grade: "))
        self._exam_grade = int(input("Enter exam grade: "))
        self._quiz_grade = int(input("Enter quiz grade: "))
        super().study()

    def calculate_average(self) -> float:
        return (self._daily_grade + self._exam_grade + self._quiz_grade) / 3

    def calculate_rank(self) -> str:
        average_grade = self.calculate_average()
        if 81 <= average_grade <= 100:
            return 'A'
        elif 61 <= average_grade <= 80:
            return 'B'
        elif 41 <= average_grade <= 60:
            return 'C'
        elif 21 <= average_grade <= 40:
            return 'D'
        elif 0 <= average_grade <= 20:
            return 'E'
        else:
            return 'Invalid Rank'

while True:
    name = input("Enter name: ")
    age = int(input("Enter age: "))

    if 19 <= age <= 27:
        student = Grades(name, age)
        student._semester = input("Enter semester: ")
        student._student_id = input("Enter student ID: ")
        student.study()

        student.display_info()
    else:
        teacher = Teacher(name, age)
        teacher._class_name = input("Enter class name: ")
        teacher._employee_id = input("Enter employee ID: ")
     
        teacher.display_info()
        teacher.teach()

   
    print(f"Name: {name}")
    print(f"Age: {age}")

    try_again = input("Do you want to try again? (yes/no): ").lower()
    if try_again != 'yes':
        break  
