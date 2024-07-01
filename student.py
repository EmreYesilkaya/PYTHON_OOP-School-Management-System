class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = []  # List of tuples (assignment_name, score)
        self.attendance = []  # List of tuples (date, present)
        self.disciplinary_actions = []  # List of strings detailing actions

    def add_grade(self, assignment_name, score):
        """Adds a grade for a specific assignment."""
        self.grades.append((assignment_name, score))

    def record_attendance(self, date, present):
        """Records attendance, 'present' is a boolean indicating if the student was present."""
        self.attendance.append((date, present))

    def record_disciplinary_action(self, action):
        """Records a disciplinary action with a description of the action."""
        self.disciplinary_actions.append(action)

    def get_average_grade(self):
        """Calculates and returns the average grade for the student."""
        if not self.grades:
            return 0  # Avoid division by zero
        total_score = sum(score for _, score in self.grades)
        return total_score / len(self.grades)

    def __str__(self):
        """Returns a string representation of the student, primarily for debugging."""
        return f"Student {self.name}, ID {self.student_id}"
