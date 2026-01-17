class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    def display(self):
        print(f"Name: {self.name}, Roll No: {self.roll}")

students = []

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Choose: ")

    if choice == "1":
        name = input("Enter name: ")
        roll = input("Enter roll: ")
        students.append(Student(name, roll))
        print("Student added")

    elif choice == "2":
        for s in students:
            s.display()

    elif choice == "3":
        break

    else:
        print("Invalid choice")
