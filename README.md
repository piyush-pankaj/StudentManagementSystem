# 🎓 Student Management System (Python OOP Project)

A **console-based Student Management System** built using **Python Object-Oriented Programming (OOP)** concepts. This project allows users to manage student records, store marks, calculate averages, and save/load student information using CSV files.

The project demonstrates the practical implementation of **Classes & Objects, Inheritance, Abstraction, Encapsulation, File Handling, Exception Handling, and Properties** in Python.

---

## 📌 Features

- ➕ Add new students
- 📚 Add subject-wise marks
- 🔍 Search student by Student ID
- ✏️ Update student information
- 🗑️ Delete student records
- 📋 Display all students
- 📊 Calculate individual student average
- 🎯 Calculate class average
- 💾 Save student records to CSV file
- 📂 Load student records from CSV file
- ⚠️ Custom exception handling
- 🔒 Data validation using properties

---

## 🛠️ Technologies Used

- Python 3.x
- Object-Oriented Programming (OOP)
- CSV File Handling
- Abstract Base Classes (ABC)
- Exception Handling

---

## 📂 Project Structure

```
StudentManagementSystem/
│
├── student_management.py
├── students.csv          # Generated after saving records
└── README.md
```

---

## 🚀 OOP Concepts Implemented

### 1. Abstraction
- `Person` is an Abstract Base Class.
- Uses the `ABC` module.
- Contains the abstract method:
  - `display_info()`

---

### 2. Inheritance

```
Person
   │
   └── Student
```

The `Student` class inherits common attributes from the `Person` class.

---

### 3. Encapsulation

Private variables are used to protect data.

Examples:

```python
__student_id
__marks
__students
__name
__age
```

Access is controlled using properties and methods.

---

### 4. Properties

The project uses Python Properties for controlled access.

Example:

```python
@property
def age(self):
    return self.__age
```

Age validation is performed before assigning values.

---

### 5. Exception Handling

Custom exceptions are implemented.

- `StudentManagementError`
- `StudentNotFoundError`
- `DuplicateStudentError`

These exceptions provide meaningful error messages and improve code readability.

---

## 📋 Menu Options

```
1. Add Student
2. Display All Students
3. Search Student
4. Update Student
5. Delete Student
6. Class Average
7. Save to CSV
8. Load from CSV
9. Exit
```

---

## 📖 How It Works

### Add Student

- Enter Student ID
- Enter Name
- Enter Age
- Enter Subject Names
- Enter Marks
- Student record is stored in memory

---

### Display Students

Displays:

- Student ID
- Name
- Age
- Subject Marks
- Average Marks

---

### Search Student

Search a student using their unique Student ID.

---

### Update Student

Modify:

- Name
- Age

---

### Delete Student

Removes the student from the system.

---

### Calculate Class Average

Calculates the average marks of all students in the system.

---

### Save Data

Stores student information into:

```
students.csv
```

---

### Load Data

Loads previously saved student records from the CSV file.

---

## 📄 CSV Format

The application stores data in the following format:

| student_id | name | age |
|------------|------|-----|
| S101 | John | 18 |
| S102 | Alice | 20 |

> **Note:** Currently, only student details (ID, Name, and Age) are saved to the CSV file. Subject marks are maintained in memory during program execution and are not persisted.

---

## ⚠️ Input Validation

The system validates user input to ensure data integrity.

### Age Validation

- Minimum Age: **5**
- Maximum Age: **50**

### Marks Validation

- Minimum Marks: **0**
- Maximum Marks: **100**

Duplicate Student IDs are not allowed.

---

## 🧩 Custom Exceptions

| Exception | Description |
|-----------|-------------|
| StudentManagementError | Base exception class |
| StudentNotFoundError | Raised when Student ID does not exist |
| DuplicateStudentError | Raised when Student ID already exists |

---

## ▶️ Running the Project

### Clone the repository

```bash
git clone <repository-url>
```

### Navigate to the project folder

```bash
cd StudentManagementSystem
```

### Run the program

```bash
python student_management.py
```

---

## 📚 Learning Outcomes

This project helps learners understand:

- Python Classes and Objects
- Abstract Classes
- Inheritance
- Encapsulation
- Properties (Getter & Setter)
- Custom Exceptions
- File Handling with CSV
- Dictionaries
- Menu-Driven Programming
- Data Validation
- Python Best Practices

---

## 🔮 Future Improvements

- Save and load subject-wise marks in CSV
- Student grade calculation
- GPA/CGPA calculation
- Sorting students by average marks
- Search by name
- Attendance management
- Multiple class support
- Report card generation
- Export to Excel or PDF
- Database integration (SQLite/MySQL)
- Graphical User Interface (Tkinter/PyQt)
- Web version using Flask or Django

---

## 👨‍💻 Author

Developed as a Python Object-Oriented Programming project to demonstrate real-world implementation of OOP concepts, file handling, and exception handling.

---

## 📜 License

This project is intended for educational and learning purposes. Feel free to modify and enhance it for your own projects.