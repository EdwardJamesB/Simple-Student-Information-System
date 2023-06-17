import csv

# Function to add a student
def add_student():
    student_data = []
    with open('students.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        student_data.append(input("Enter ID Number: "))
        student_data.append(input("Enter First Name: "))
        student_data.append(input("Enter Last Name: "))
        student_data.append(input("Enter Gender: "))
        student_data.append(input("Enter Year: "))
        student_data.append(input("Enter Course: "))
        writer.writerow(student_data)
    print("Student added successfully.")

# Function to add a course
def add_course():
    course_data = []
    with open('courses.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        course_data.append(input("Enter ID: "))
        course_data.append(input("Enter Name: "))
        course_data.append(input("Enter Code: "))
        writer.writerow(course_data)
    print("Course added successfully.")

# Function to delete a student
def delete_student():
    student_id = input("Enter the ID Number of the student to delete: ")
    rows_deleted = 0
    with open('students.csv', 'r', newline='') as file:
        reader = csv.reader(file)
        rows = list(reader)
    with open('students.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for row in rows:
            if row[0] != student_id:
                writer.writerow(row)
            else:
                rows_deleted += 1
    if rows_deleted > 0:
        print(f"Deleted {rows_deleted} student(s) successfully.")
    else:
        print("Student not found.")

# Function to delete a course
def delete_course():
    course_id = input("Enter the ID of the course to delete: ")
    rows_deleted = 0
    with open('courses.csv', 'r', newline='') as file:
        reader = csv.reader(file)
        rows = list(reader)
    with open('courses.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for row in rows:
            if row[0] != course_id:
                writer.writerow(row)
            else:
                rows_deleted += 1
    if rows_deleted > 0:
        print(f"Deleted {rows_deleted} course(s) successfully.")

# Function to edit a student
def edit_student():
    student_id = input("Enter the ID Number of the student to edit: ")
    with open('students.csv', 'r', newline='') as file:
        reader = csv.reader(file)
        rows = list(reader)
    with open('students.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for row in rows:
            if row[0] == student_id:
                row[1] = input("Enter First Name: ")
                row[2] = input("Enter Last Name: ")
                row[3] = input("Enter Gender: ")
                row[4] = input("Enter Year: ")
            writer.writerow(row)
    print("Student edited successfully.")

# Function to list students
def list_students():
    with open('students.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

# Function to list courses
def list_courses():
    with open('courses.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

# Function to search student by name
def search_student_by_name():
    search_name = input("Enter the name of the student to search: ")
    found_students = []
    with open('students.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[1].lower() == search_name.lower():
                found_students.append(row)

    if found_students:
        for student in found_students:
            print(student)
    else:
        print("No student found with the given name.")

# Function to search student by ID Number
def search_student_by_id():
    search_id = input("Enter the ID Number of the student to search: ")
    found_students = []
    with open('students.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == search_id:
                found_students.append(row)
    if found_students:
        for student in found_students:
            print(student)
    else:
        print("No student found with the given ID Number.")

# Main menu
def main_menu():
    while True:
        print("\n--- Student Information System ---")
        print("1. Add Student")
        print("2. Add Course")
        print("3. Delete Student")
        print("4. Delete Course")
        print("5. Edit Student")
        print("6. List Students")
        print("7. List Courses")
        print("8. Search Student by Name")
        print("9. Search Student by ID")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_student()
        elif choice == '2':
            add_course()
        elif choice == '3':
            delete_student()
        elif choice == '4':
            delete_course()
        elif choice == '5':
            edit_student()
        elif choice == '6':
            list_students()
        elif choice == '7':
            list_courses()
        elif choice == '8':
            search_student_by_name()
        elif choice == '9':
            search_student_by_id()
        elif choice == '0':
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
main_menu()