# Husky Card Management System using a dictionary
students = {}


# Function to add a new student with their subjects
def add_student(name, subjects):
    if name in students:
        print(f"Student '{name}' already exists.")
    else:
        students[name] = subjects
        print(f"Student '{name}' added successfully!")


# Function to modify a student's subject list by replacing an old subject with a new one
def modify_subject(name, old_subject, new_subject):
    if name in students:
        if old_subject in students[name]:
            students[name].remove(old_subject)
            students[name].append(new_subject)
            print(f"Replaced '{old_subject}' with '{new_subject}' for student '{name}'.")
        else:
            print(f"'{old_subject}' is not in the list of subjects for student '{name}'.")
    else:
        print(f"Student '{name}' does not exist.")


# Function to remove a specific subject from a student's list
def remove_subject(name, subject):
    if name in students:
        if subject in students[name]:
            students[name].remove(subject)
            print(f"Removed subject '{subject}' from student '{name}'.")
        else:
            print(f"'{subject}' not found in the subjects list of student '{name}'.")
    else:
        print(f"Student '{name}' does not exist.")


# Function to display all students enrolled in a specific subject
def display_students_in_subject(subject):
    enrolled_students = [name for name, subjects in students.items() if subject in subjects]
    if enrolled_students:
        print(f"Students enrolled in '{subject}': {', '.join(enrolled_students)}")
    else:
        print(f"No students are currently enrolled in '{subject}'.")


# Function to list all students along with their subjects, sorted alphabetically by student name
def list_all_students():
    if students:
        print("Students and their subjects (sorted by name):")
        for name in sorted(students):
            print(f"Student: {name}, Subjects: {', '.join(students[name])}")
    else:
        print("No students in the system.")


# Sample menu to interact with the Husky Card Management System
def husky_card_menu():
    while True:
        print("\nHusky Card Management System Menu:")
        print("1. Add new student")
        print("2. Modify student's subject")
        print("3. Remove a subject from a student")
        print("4. Display students in a specific subject")
        print("5. List all students and their subjects")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == '1':
            name = input("Enter the student's name: ")
            subjects = input("Enter subjects (separated by commas): ").split(',')
            subjects = [subject.strip() for subject in subjects]  # Removing any extra spaces
            add_student(name, subjects)
        elif choice == '2':
            name = input("Enter the student's name: ")
            old_subject = input("Enter the old subject to replace: ")
            new_subject = input("Enter the new subject: ")
            modify_subject(name, old_subject, new_subject)
        elif choice == '3':
            name = input("Enter the student's name: ")
            subject = input("Enter the subject to remove: ")
            remove_subject(name, subject)
        elif choice == '4':
            subject = input("Enter the subject: ")
            display_students_in_subject(subject)
        elif choice == '5':
            list_all_students()
        elif choice == '6':
            print("Exiting the Husky Card Management System.")
            break
        else:
            print("Invalid choice, please select again.")


# Running the Husky Card Management System menu
if __name__ == '__main__':
    husky_card_menu()