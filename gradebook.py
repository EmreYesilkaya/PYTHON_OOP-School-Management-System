from student import Student

class GradeBook:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        """Adds a new student to the gradebook."""
        self.students.append(student)
        print(f"{student.name} has been added to the gradebook.")

    def find_student(self, student_id):
        """Finds a student by their ID."""
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None

    def add_grade_to_student(self, student_id, assignment_name, score):
        """Adds a grade to a student's record."""
        student = self.find_student(student_id)
        if student:
            student.add_grade(assignment_name, score)
            print(f"Grade {score} for {assignment_name} added to {student.name}'s record.")
        else:
            print("Student not found.")
