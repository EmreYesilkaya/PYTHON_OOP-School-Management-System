class StudentReport:
    @staticmethod
    def generate_grade_report(student):
        report = [f"Grades Report for {student.name} (ID: {student.student_id}):"]
        if student.grades:
            average = student.get_average_grade()
            report.append("Details of Grades:")
            for assignment, grade in student.grades:
                report.append(f"{assignment}: {grade}")
            report.append(f"Average Grade: {average:.2f}")
        else:
            report.append("No grades recorded.")
        return "\n".join(report)

    @staticmethod
    def generate_attendance_report(student):
        report = [f"Attendance Report for {student.name} (ID: {student.student_id}):"]
        if student.attendance:
            total_present = sum(1 for _, present in student.attendance if present)
            total_days = len(student.attendance)
            attendance_rate = (total_present / total_days) * 100
            report.append("Attendance Details:")
            for date, present in student.attendance:
                status = "Present" if present else "Absent"
                report.append(f"{date}: {status}")
            report.append(f"Attendance Rate: {attendance_rate:.2f}%")
        else:
            report.append("No attendance records.")
        return "\n".join(report)

    @staticmethod
    def generate_disciplinary_report(student):
        report = [f"Disciplinary Report for {student.name} (ID: {student.student_id}):"]
        if student.disciplinary_actions:
            report.append("Recorded Disciplinary Actions:")
            for action in student.disciplinary_actions:
                report.append(action)
        else:
            report.append("No disciplinary actions recorded.")
        return "\n".join(report)
