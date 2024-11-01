# student_management_system
import json
from person import Student
from course import Course

class StudentManagementSystem:
    def __init__(self):
        self.__students = {}
        self.__courses = {}

    def add_student(self, name: str, age: int, address: str, student_id: str):
        if student_id not in self.__students:
            self.__students[student_id] = Student(name, age, address, student_id)
            print(f"Student {name} (ID: {student_id}) added successfully.")
        else:
            print("Student ID already exists.")

    def add_course(self, course_name: str, course_code: str, instructor: str):
        if course_code not in self.__courses:
            self.__courses[course_code] = Course(course_name, course_code, instructor)
            print(f"Course {course_name} (Code: {course_code}) created with instructor {instructor}.")
        else:
            print("Course code already exists.")

    def enroll_student_in_course(self, student_id: str, course_code: str):
        student = self.__students.get(student_id)
        course = self.__courses.get(course_code)
        if student and course:
            course.add_student(student)
            print(f"Student {student.name} (ID: {student_id}) enrolled in {course.course_name} (Code: {course_code}).")
        else:
            print("Invalid student ID or course code.")

    def add_grade_for_student(self, student_id: str, course_code: str, grade: str):
        student = self.__students.get(student_id)
        course = self.__courses.get(course_code)
        if student and course and course.course_name in student.courses:
            student.add_grade(course.course_name, grade)
            print(f"Grade {grade} added for {student.name} in {course.course_name}.")
        else:
            print("Cannot add grade. Either student or course does not exist, or student is not enrolled.")

    def display_student_details(self, student_id: str):
        student = self.__students.get(student_id)
        if student:
            student.display_student_info()
        else:
            print("Student not found.")

    def display_course_details(self, course_code: str):
        course = self.__courses.get(course_code)
        if course:
            course.display_course_info()
        else:
            print("Course not found.")

    
    #Save data to json file
    def save_data(self, filename="data.json"):
        data = {
            "students": {
                id: {
                    "name": s.name,
                    "age": s._Person__age,
                    "address": s._Person__address,
                    "student_id": s.student_id,
                    "courses": s.courses,
                    "grades": s._Student__grades
                } for id, s in self.__students.items()
            },
            "courses": {
                code: {
                    "course_name": c.course_name,
                    "course_code": c.course_code,
                    "instructor": c._Course__instructor,
                    "students": [s.student_id for s in c.students]
                } for code, c in self.__courses.items()
            }
        }
        with open(filename, "w") as file:
            json.dump(data, file)
        print("Data saved successfully.")

    #Load data from json file
    def load_data(self, filename="data.json"):
        try:
            with open(filename, "r") as file:
                data = json.load(file)

                # Load students
                for student_id, details in data["students"].items():
                    student = Student(
                        name=details["name"],
                        age=details["age"],
                        address=details["address"],
                        student_id=student_id
                    )
                    student._Student__grades = details["grades"]
                    for course in details["courses"]:
                        student.enroll_course(course,showMsg = False)
                        
                    self.__students[student_id] = student

                # Load courses
                for course_code, details in data["courses"].items():
                    course = Course(
                        course_name=details["course_name"],
                        course_code=details["course_code"],
                        instructor=details["instructor"]
                    )
                    # Enroll students in course based on loaded data
                    for student_id in details["students"]:
                        student = self.__students.get(student_id)
                        if student:
                            course.add_student(student)
                    self.__courses[course_code] = course

            print("Data loaded successfully.")
        except FileNotFoundError:
            print("Data file not found.")
        except Exception as e:
            print(f"An error occurred while loading data: {e}")
