# main.py
from gradebook import GradeBook
from student import Student
from student_report import StudentReport

class SchoolManagementSystem:
    def __init__(self):
        self.gradebook = GradeBook()

    def add_student(self):
        name = input("Enter student name: ")
        student_id = input("Enter student ID: ")
        new_student = Student(name, student_id)
        self.gradebook.add_student(new_student)
        print("Student added successfully.")

    def student_menu(self, student):
        while True:
            print("\n1. Add Grade")
            print("2. Record Attendance")
            print("3. Record Disciplinary Action")
            print("4. Generate Reports")
            print("5. Return to Main Menu")
            choice = input("Choose an action: ")
            if choice == "1":
                self.add_grade(student)
            elif choice == "2":
                self.record_attendance(student)
            elif choice == "3":
                self.record_disciplinary_action(student)
            elif choice == "4":
                self.generate_reports(student)
            elif choice == "5":
                break
            else:
                print("Invalid action selected. Please try again.")

    def add_grade(self, student):
        assignment_name = input("Enter assignment name: ")
        score = float(input("Enter score: "))
        student.add_grade(assignment_name, score)
        print("Grade added successfully.")

    def record_attendance(self, student):
        date = input("Enter date (YYYY-MM-DD): ")
        present = input("Present (yes/no): ").lower() == 'yes'
        student.record_attendance(date, present)
        print("Attendance recorded.")

    def record_disciplinary_action(self, student):
        action = input("Enter disciplinary action: ")
        student.record_disciplinary_action(action)
        print("Disciplinary action recorded.")

    def generate_reports(self, student):
        print(StudentReport.generate_grade_report(student))
        print(StudentReport.generate_attendance_report(student))
        print(StudentReport.generate_disciplinary_report(student))

    def run(self):
        while True:
            print("\n1. Add Student")
            print("2. Manage Student")
            print("3. Exit")
            choice = input("Choose an option: ")
            if choice == "1":
                self.add_student()
            elif choice == "2":
                student_id = input("Enter student ID to manage: ")
                student = self.gradebook.find_student(student_id)
                if student:
                    self.student_menu(student)
                else:
                    print("Student not found.")
            elif choice == "3":
                print("Exiting...")
                break
            else:
                print("Invalid option, please try again.")

if __name__ == "__main__":
    sms = SchoolManagementSystem()
    sms.run()
