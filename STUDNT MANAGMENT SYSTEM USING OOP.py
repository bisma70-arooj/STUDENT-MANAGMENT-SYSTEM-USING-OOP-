class Student:
    all_students = []

    def __init__(self, name, roll_num, marks):
        self.name = name
        self.roll_num = roll_num
        self.marks = marks

    def update_marks(self, new_marks):
        self.marks = new_marks
        print(f"Marks updated to {new_marks} for student {self.name}.")

    def show_details(self):
        print("\n======= STUDENT DETAILS =========")
        print(
            f"Name: {self.name}, Roll Number: {self.roll_num}, Marks: {self.marks}"
        )

    @classmethod
    def find_student_by_roll_num(cls, roll_num):
        for student in cls.all_students:
            if student.roll_num == roll_num:
                return student
        return None

    @classmethod
    def add_student(cls):
        name = input("Enter student name: ").strip()
        roll_num = input("Enter roll number: ").strip()

        # Check for duplicate roll number
        if cls.find_student_by_roll_num(roll_num):
            print("A student with this roll number already exists.")
            return

        try:
            marks = float(input("Enter marks: "))
        except ValueError:
            print("Invalid input for marks. Student not added.")
            return

        student = cls(name, roll_num, marks)
        cls.all_students.append(student)
        print(f"Student {name} added successfully.")

    @classmethod
    def update_student_marks(cls):
        roll_num = input("Enter student roll number to update marks: ").strip()
        student = cls.find_student_by_roll_num(roll_num)

        if student:
            try:
                new_marks = float(input("Enter New Marks: "))
                student.update_marks(new_marks)
            except ValueError:
                print("Invalid input for marks. Marks not updated.")
        else:
            print("Student not found.")

    @classmethod
    def show_all_students(cls):
        if not cls.all_students:
            print("No students found.")
        else:
            for student in cls.all_students:
                student.show_details()


def menu():
    while True:
        print("\n============= STUDENT MANAGEMENT SYSTEM =============")
        print("1. Add Student")
        print("2. Update Marks")
        print("3. Show all students")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice (1-4): "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            continue

        if choice == 1:
            Student.add_student()
        elif choice == 2:
            Student.update_student_marks()
        elif choice == 3:
            Student.show_all_students()
        elif choice == 4:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    menu()        



