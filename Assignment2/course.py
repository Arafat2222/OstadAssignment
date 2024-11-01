# course
from person import Student

class Course:
    def __init__(self, course_name: str, course_code: str, instructor: str):
        self.__course_name = course_name
        self.__course_code = course_code
        self.__instructor = instructor
        self.__students = []

    def add_student(self, student: Student):
        if student not in self.__students:
            self.__students.append(student)
            student.enroll_course(self.__course_name,showMsg=False)
        else:
            
            print("Student already enrolled in this course.")

    def display_course_info(self):
        print("Course information:")
        print(f"Course Name: {self.__course_name}")
        print(f"Course Code: {self.__course_code}")
        print(f"Instructor: {self.__instructor}")
        print("Enrolled Students:", ", ".join([s.name for s in self.__students]))

    # Getters for private attributes
    @property
    def course_name(self):
        return self.__course_name

    @property
    def course_code(self):
        return self.__course_code

    @property
    def students(self):
        return self.__students
