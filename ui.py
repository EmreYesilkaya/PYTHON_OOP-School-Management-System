import tkinter as tk
from tkinter import messagebox, Toplevel
from school_management_system import SchoolManagementSystem
from student import Student
from student_report import StudentReport
from PIL import Image, ImageTk

system = SchoolManagementSystem()

def register_student():
    def save_new_student():
        name = name_entry.get()
        student_id = id_entry.get()
        if name and student_id:
            new_student = Student(name, student_id)
            system.gradebook.add_student(new_student)
            messagebox.showinfo("Success", "Student registered successfully")
            register_window.destroy()
        else:
            messagebox.showerror("Error", "Name and ID must be filled out")

    register_window = Toplevel(root)
    register_window.title("Register New Student")
    tk.Label(register_window, text="Student Name:").grid(row=0, column=0)
    name_entry = tk.Entry(register_window)
    name_entry.grid(row=0, column=1)
    tk.Label(register_window, text="Student ID:").grid(row=1, column=0)
    id_entry = tk.Entry(register_window)
    id_entry.grid(row=1, column=1)
    save_btn = tk.Button(register_window, text="Register", command=save_new_student)
    save_btn.grid(row=2, column=0, columnspan=2)

def open_student_data_window(student, data_type):
    def save_data():
        if data_type == 'grade':
            assignment = assignment_entry.get()
            score = score_entry.get()
            if assignment and score:
                try:
                    student.add_grade(assignment, float(score))
                    messagebox.showinfo("Success", f"Grade {score} added to {assignment}")
                    data_window.destroy()
                except ValueError:
                    messagebox.showerror("Error", "Score must be a number")
        elif data_type == 'attendance':
            date = date_entry.get()
            present = present_entry.get().lower() == 'yes'
            student.record_attendance(date, present)
            messagebox.showinfo("Success", "Attendance recorded")
            data_window.destroy()
        elif data_type == 'disciplinary':
            action = action_entry.get()
            student.record_disciplinary_action(action)
            messagebox.showinfo("Success", "Disciplinary action recorded")
            data_window.destroy()

    data_window = Toplevel(root)
    data_window.title(f"{data_type.capitalize()} Data - {student.name}")
    if data_type == 'grade':
        tk.Label(data_window, text="Assignment:").grid(row=0, column=0)
        assignment_entry = tk.Entry(data_window)
        assignment_entry.grid(row=0, column=1)
        tk.Label(data_window, text="Score:").grid(row=1, column=0)
        score_entry = tk.Entry(data_window)
        score_entry.grid(row=1, column=1)
    elif data_type == 'attendance':
        tk.Label(data_window, text="Date:").grid(row=0, column=0)
        date_entry = tk.Entry(data_window)
        date_entry.grid(row=0, column=1)
        tk.Label(data_window, text="Present (Yes/No):").grid(row=1, column=0)
        present_entry = tk.Entry(data_window)
        present_entry.grid(row=1, column=1)
    elif data_type == 'disciplinary':
        tk.Label(data_window, text="Disciplinary Action:").grid(row=0, column=0)
        action_entry = tk.Entry(data_window)
        action_entry.grid(row=0, column=1)
    save_btn = tk.Button(data_window, text="Save", command=save_data)
    save_btn.grid(row=2, column=0, columnspan=2)

def generate_full_report(student):
    grade_report = StudentReport.generate_grade_report(student)
    attendance_report = StudentReport.generate_attendance_report(student)
    disciplinary_report = StudentReport.generate_disciplinary_report(student)
    full_report = "\n\n".join([grade_report, attendance_report, disciplinary_report])
    messagebox.showinfo(f"Full Report for {student.name}", full_report)

def search_and_open_data_type(data_type):
    student_id = id_entry.get()
    student = system.gradebook.find_student(student_id)
    if student:
        if data_type == 'reports':
            generate_full_report(student)
        else:
            open_student_data_window(student, data_type)
    else:
        messagebox.showerror("Error", "Student not found")

root = tk.Tk()
root.title("School Management System")

# Resmi ekleyelim
image_path = "photo/Vilnius_university_logo.svg.png"
image = Image.open(image_path)
# Resmi küçültelim
image = image.resize((200, 200))
photo = ImageTk.PhotoImage(image)
image_label = tk.Label(root, image=photo)
image_label.grid(row=0, column=0, columnspan=2)

# Metin giriş alanını üstüne yerleştirelim
tk.Label(root, text="Student ID:").grid(row=1, column=0)
id_entry = tk.Entry(root)
id_entry.grid(row=1, column=1)

# Diğer bileşenlerin konumunu güncelleyelim
search_grade_btn = tk.Button(root, text="Add Grade", command=lambda: search_and_open_data_type('grade'))
search_grade_btn.grid(row=2, column=0)
search_attendance_btn = tk.Button(root, text="Add Attendance", command=lambda: search_and_open_data_type('attendance'))
search_attendance_btn.grid(row=2, column=1)
search_disciplinary_btn = tk.Button(root, text="Add Disciplinary", command=lambda: search_and_open_data_type('disciplinary'))
search_disciplinary_btn.grid(row=3, column=0)
search_reports_btn = tk.Button(root, text="Generate Reports", command=lambda: search_and_open_data_type('reports'))
search_reports_btn.grid(row=3, column=1)
register_btn = tk.Button(root, text="Register New Student", command=register_student)
register_btn.grid(row=4, column=0, columnspan=2)

root.mainloop()
