# person

class Person:
    def __init__(self, name: str, age: int, address: str):
        self.__name = name
        self.__age = age
        self.__address = address
    
    def display_person_info(self):
        print(f"Name: {self.__name}")
        print(f"Age: {self.__age}")
        print(f"Address: {self.__address}")

    # Getters for private attributes
    @property
    def name(self):
        return self.__name


class Student(Person):
    
    def __init__(self, name: str, age: int, address: str, student_id: str):
        super().__init__(name, age, address)
        self.__student_id = student_id
        self.__grades = {}
        self.__courses = []
        
    def add_grade(self, subject: str, grade: str):
        if subject in self.__courses:
            self.__grades[subject] = grade
        else:
            print(f"Cannot add grade. Student is not enrolled in {subject}.")

    def enroll_course(self, course: str,showMsg = True):
       
        #print(showMsg)
        if course not in self.__courses:
            self.__courses.append(course)
        if showMsg:
            #pass
            print(f"Already enrolled in {course}")

    def display_student_info(self):
        print("Student Information:")
        self.display_person_info()
        print(f"Student ID: {self.__student_id}")
        print("Enrolled Courses:", ", ".join(self.__courses))
        print("Grades:", self.__grades)

    # Getters for private attributes
    @property
    def student_id(self):
        return self.__student_id

    @property
    def courses(self):
        return self.__courses
