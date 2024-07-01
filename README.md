# School Management System

![Vilnius University Logo](Vilnius_university_logo.svg.png)

## Overview

The School Management System is a comprehensive application designed to manage various aspects of student information. This system allows administrators to add new students, record their academic performance, track attendance, manage disciplinary actions, and generate detailed reports.

## Features

- **Student Management**: Efficiently add and manage student information.
- **Grade Management**: Record and view grades for various assignments and exams.
- **Attendance Tracking**: Monitor student attendance over time.
- **Disciplinary Actions**: Keep records of disciplinary actions taken.
- **Report Generation**: Generate comprehensive reports on grades, attendance, and disciplinary actions.

## Getting Started

### Prerequisites

To run this project, you need to have the following installed:

- Python 3.x
- pip (Python package installer)

### Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/school-management-system.git
    cd school-management-system
    ```

2. **Install the required packages**:
    ```sh
    pip install -r requirements.txt
    ```

3. **Run the application**:
    ```sh
    python ui.py
    ```

## Project Structure

The project is structured into several modules, each handling specific aspects of the system:

### GradeBook

This module is responsible for managing the list of students and their grades. It includes functionalities to add students, find students by ID, and record grades.

### Student

This module defines the `Student` class, encapsulating student details such as name, ID, grades, attendance, and disciplinary actions. It provides methods to add grades, record attendance, and manage disciplinary actions.

### StudentReport

This module includes methods to generate detailed reports for students. It can generate reports for grades, attendance, and disciplinary actions, providing a comprehensive overview of a student's performance and behavior.

### SchoolManagementSystem

This module integrates the functionalities of the other modules and provides a command-line interface (CLI) for interaction. It includes methods to add students, manage student records, and generate reports.

### User Interface (UI)

The `ui.py` module provides a graphical user interface (GUI) using Tkinter. It allows users to register new students, record data, and generate reports through an intuitive interface.

## How to Use

1. **Register New Students**:
   - Open the application.
   - Click on "Register New Student".
   - Enter the student's name and ID, then click "Register".

2. **Manage Student Data**:
   - Enter the student's ID and select the action you want to perform (Add Grade, Add Attendance, Add Disciplinary, Generate Reports).

3. **Generate Reports**:
   - Select "Generate Reports" to view a comprehensive report of the student's grades, attendance, and disciplinary actions.

## Contributing

We welcome contributions to enhance the functionalities and features of the School Management System. To contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Acknowledgments

- Vilnius University for their support and resources.
- All contributors and users of this project.

For any queries or support, please contact us at [your-email@example.com].

