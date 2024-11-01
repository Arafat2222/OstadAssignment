# cli
from manage import StudentManagementSystem
def main():
    sms = StudentManagementSystem()
    while True:
        print("==== Student Management System ====")
        print("1. Add New Student")
        print("2. Add New Course")
        print("3. Enroll Student in Course")
        print("4. Add Grade for Student")
        print("5. Display Student Details")
        print("6. Display Course Details")
        print("7. Save Data to File")
        print("8. Load Data from File")
        print("0. Exit")
        option = input("Select Option: ")

        if option == '1':
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            address = input("Enter Address: ")
            student_id = input("Enter Student ID: ")
            sms.add_student(name, age, address, student_id)
        elif option == '2':
            course_name = input("Enter Course Name: ")
            course_code = input("Enter Course Code: ")
            instructor = input("Enter Instructor Name: ")
            sms.add_course(course_name, course_code, instructor)
        elif option == '3':
            student_id = input("Enter Student ID: ")
            course_code = input("Enter Course Code: ")
            sms.enroll_student_in_course(student_id, course_code)
        elif option == '4':
            student_id = input("Enter Student ID: ")
            course_code = input("Enter Course Code: ")
            grade = input("Enter Grade: ")
            sms.add_grade_for_student(student_id, course_code, grade)
        elif option == '5':
            student_id = input("Enter Student ID: ")
            sms.display_student_details(student_id)
        elif option == '6':
            course_code = input("Enter Course Code: ")
            sms.display_course_details(course_code)
        elif option == '7':
            sms.save_data()
        elif option == '8':
            sms.load_data()
        elif option == '0':
            print("Exiting Student Management System. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
