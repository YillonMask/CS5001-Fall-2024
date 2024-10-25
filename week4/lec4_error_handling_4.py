def read_grades(filename):
    grades = {}
    try:
        with open(filename, "r") as file:
            for line in file:
                name, grade = line.strip().split(",")
                grades[name] = float(grade)
    except FileNotFoundError:
        print(f"File {filename} not found. Starting with an empty grade book.")
    except ValueError:
        print("Error reading file. Make sure it's in the correct format.")
    return grades


def write_grades(filename, grades):
    with open(filename, "w") as file:
        for name, grade in grades.items():
            file.write(f"{name},{grade}\n")


def display_grades(grades):
    if not grades:
        print("No grades to display.")
    else:
        print("Current grades:")
        for name, grade in grades.items():
            print(f"{name}: {grade}")


def add_student(grades):
    name = input("Enter student name: ")
    while True:
        try:
            grade = float(input("Enter student grade: "))
            break
        except ValueError:
            print("Invalid input. Please enter a numeric grade.")
    grades[name] = grade
    print(f"Added {name} with grade {grade}")


def update_grade(grades):
    name = input("Enter student name to update: ")
    if name in grades:
        while True:
            try:
                new_grade = float(input("Enter new grade: "))
                break
            except ValueError:
                print("Invalid input. Please enter a numeric grade.")
        grades[name] = new_grade
        print(f"Updated {name}'s grade to {new_grade}")
    else:
        print(f"Student {name} not found.")


def main():
    filename = "student_grades.txt"
    grades = read_grades(filename)

    while True:
        print("\n1. Display grades")
        print("2. Add a new student")
        print("3. Update a student's grade")
        print("4. Save and exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            display_grades(grades)
        elif choice == "2":
            add_student(grades)
        elif choice == "3":
            update_grade(grades)
        elif choice == "4":
            write_grades(filename, grades)
            print("Grades saved. Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
