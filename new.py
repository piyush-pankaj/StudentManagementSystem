from abc import ABC, abstractmethod
import csv


# Custom Exceptions 
class StudentManagementError(Exception):
    pass


class StudentNotFoundError(StudentManagementError):
    def __init__(self, student_id):
        super().__init__(f"Student with ID '{student_id}' not found.")


class DuplicateStudentError(StudentManagementError):
    def __init__(self, student_id):
        super().__init__(f"Student with ID '{student_id}' already exists.")


# Person (Abstract Base Class)
class Person(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if not (5 <= value <= 50):
            raise ValueError("Age must be between 5 and 50.")
        self.__age = value

    @abstractmethod
    def display_info(self):
        pass


# Student Class
class Student(Person):
    def __init__(self, student_id, name, age):
        super().__init__(name, age)
        self.__student_id = student_id
        self.__marks = {}

    @property
    def student_id(self):
        return self.__student_id

    def add_mark(self, subject, score):
        if not (0 <= score <= 100):
            raise ValueError("Score must be between 0 and 100.")
        self.__marks[subject] = score

    def calculate_average(self):
        if not self.__marks:
            return 0
        return sum(self.__marks.values()) / len(self.__marks)

    def display_info(self):
        return (f"ID: {self.__student_id}, Name: {self.name}, Age: {self.age}, "
                f"Marks: {self.__marks}, Average: {self.calculate_average()}")


# ---------------- StudentManagementSystem ----------------
class StudentManagementSystem:
    def __init__(self):
        self.__students = {}

    def add_student(self, student):
        if student.student_id in self.__students:
            raise DuplicateStudentError(student.student_id)
        self.__students[student.student_id] = student

    def display_all(self):
        for student in self.__students.values():
            print(student.display_info())

    def search_student(self, student_id):
        if student_id not in self.__students:
            raise StudentNotFoundError(student_id)
        return self.__students[student_id]

    def update_student(self, student_id, name=None, age=None):
        student = self.search_student(student_id)
        if name:
            student.name = name
        if age:
            student.age = age

    def delete_student(self, student_id):
        student = self.search_student(student_id)
        del self.__students[student_id]

    def class_average(self):
        if not self.__students:
            return 0
        averages = [s.calculate_average() for s in self.__students.values()]
        return sum(averages) / len(averages)

    def save_to_file(self, filename):
        with open(filename, mode="w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["student_id", "name", "age"])
            for s in self.__students.values():
                writer.writerow([s.student_id, s.name, s.age])

    def load_from_file(self, filename):
        with open(filename, mode="r", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                student = Student(row["student_id"], row["name"], int(row["age"]))
                self.__students[student.student_id] = student


# ---------------- Menu ----------------
def menu():
    system = StudentManagementSystem()

    while True:
        print("\n1. Add Student\n2. Display All\n3. Search\n4. Update\n5. Delete\n6. Class Average\n7. Save\n8. Load\n9. Exit")
        choice = input("Enter choice: ")

        try:
            if choice == "1":
                sid = input("ID: ")
                name = input("Name: ")
                age = int(input("Age: "))
                student = Student(sid, name, age)

                while True:
                    subject = input("Subject (blank to stop): ")
                    if not subject:
                        break
                    score = float(input(f"Marks for {subject}: "))
                    student.add_mark(subject, score)

                system.add_student(student)
                print("Added!")

            elif choice == "2":
                system.display_all()

            elif choice == "3":
                sid = input("ID to search: ")
                print(system.search_student(sid).display_info())

            elif choice == "4":
                sid = input("ID to update: ")
                name = input("New name (blank to skip): ")
                age = input("New age (blank to skip): ")
                system.update_student(sid, name or None, int(age) if age else None)
                print("Updated!")

            elif choice == "5":
                sid = input("ID to delete: ")
                system.delete_student(sid)
                print("Deleted!")

            elif choice == "6":
                print("Class average:", system.class_average())

            elif choice == "7":
                system.save_to_file("students.csv")
                print("Saved!")

            elif choice == "8":
                system.load_from_file("students.csv")
                print("Loaded!")

            elif choice == "9":
                break

            else:
                print("Invalid choice.")

        except (ValueError, StudentManagementError) as e:
            print("Error:", e)


if __name__ == "__main__":
    menu()