import csv

# Function to add a student
def add_student():
    student_data = []

    # Get input data from user
    student_data.append(input("Enter ID Number: "))

    # Read existing data from CSV
    with open('students.csv', 'r', newline='') as file:
        reader = csv.reader(file)
        existing_data = list(reader)

    # Check if input ID already exists
    for row in existing_data:
        if len(row) > 0 and student_data[0] == row[0]:  # Add a check for row length
            print("Student with ID Number", student_data[0], "already exists.")
            input("Press Enter to return to the main menu...")
            return

    # Collect remaining input data
    student_data.append(input("Enter First Name: "))
    student_data.append(input("Enter Last Name: "))
    student_data.append(input("Enter Gender: "))
    student_data.append(input("Enter Year: "))
    student_data.append(input("Enter Course: "))

    # Append new student data to CSV
    with open('students.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(student_data)

    print("Student added successfully.")
    input("Press Enter to return to the main menu...")


# Function to add a course
def add_course():
    course_data = []

    # Get input data from user
    course_data.append(input("Enter Course Code: "))

    # Read existing data from CSV
    with open('courses.csv', 'r', newline='') as file:
        reader = csv.reader(file)
        existing_data = list(reader)

    # Check if input course code already exists
    for row in existing_data:
        if len(row) > 0 and course_data[0] == row[0]:  # Add a check for row length
            print("Course with Code", course_data[0], "already exists.")
            input("Press Enter to return to the main menu...")
            return

    # Collect remaining input data
    course_data.append(input("Enter Course Name: "))
    course_data.append(input("Enter College: "))

    # Append new course data to CSV
    with open('courses.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(course_data)

    print("Course added successfully.")
    input("Press Enter to return to the main menu...")

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

    input("Press Enter to return to the main menu...")

# Function to delete course
def delete_course():
    course_id = input("Enter the Course Name of the course to delete: ")
    rows_deleted = 0
    course_found = False
    associated_courses_found = False  # New flag variable

    # Delete course from courses.csv
    with open('courses.csv', 'r', newline='') as course_file:
        course_reader = csv.reader(course_file)
        courses = list(course_reader)

    with open('courses.csv', 'w', newline='') as course_file:
        course_writer = csv.writer(course_file)
        for row in courses:
            if row[1] != course_id:
                course_writer.writerow(row)
            else:
                rows_deleted += 1
                course_found = True

    # Delete course from students.csv
    with open('students.csv', 'r', newline='') as student_file:
        student_reader = csv.reader(student_file)
        students = list(student_reader)

    with open('students.csv', 'w', newline='') as student_file:
        student_writer = csv.writer(student_file)
        student_writer.writerow(students[0])  # Write the header row

        for student in students[1:]:
            if student[5] == course_id:
                student[5] = ''  # Remove the course
                associated_courses_found = True  # Set the flag if an associated course is found

            student_writer.writerow(student)

    if course_found and rows_deleted > 0:
        if associated_courses_found:
            print(f"Deleted {rows_deleted} course(s) and removed the associated course from the student records successfully.")
        else:
            print(f"Deleted {rows_deleted} course(s) successfully.")
    else:
        print("Course not found.")

    input("Press Enter to return to the main menu...")

# Function to edit a student
def edit_student():
    student_id = input("Enter the ID Number of the student to edit: ")
    found = False  # Flag to track if the student is found

    with open('students.csv', 'r', newline='') as file:
        reader = csv.reader(file)
        rows = list(reader)

    with open('students.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for row in rows:
            if row[0] == student_id:
                found = True
                row[1] = input("Enter First Name: ")
                row[2] = input("Enter Last Name: ")
                row[3] = input("Enter Gender: ")
                row[4] = input("Enter Year: ")
                row[5] = input("Enter Course: ")
            writer.writerow(row)

    if found:
        print("Student edited successfully.")
    else:
        print("No student found with ID number:", student_id)

    input("Press Enter to return to the main menu...")

# Function to edit a course
def edit_course():
    course_code = input("Enter the Course Code of the course to edit: ")
    found = False  # Flag to track if the course is found

    with open('courses.csv', 'r', newline='') as file:
        reader = csv.reader(file)
        rows = list(reader)

    with open('courses.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for row in rows:
            if row[0] == course_code:
                found = True
                row[1] = input("Enter Course Name: ")
                row[2] = input("Enter College: ")
            writer.writerow(row)

    if found:
        print("Course edited successfully.")
    else:
        print("No course found with Course Code:", course_code)

    input("Press Enter to return to the main menu...")

# Function to list students
def list_students():
    with open('students.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
    
    input("Press Enter to return to the main menu...")

# Function to list courses
def list_courses():
    with open('courses.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

    input("Press Enter to return to the main menu...")

# Function to search student by name
def search_student_by_name():
    search_name = input("Enter the name of the student to search: ")
    found_students = []

    with open('students.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            full_name_parts = row[1].split()  # Split the full name into parts
            for name_part in full_name_parts:
                if name_part.lower().startswith(search_name.lower()):
                    found_students.append(row)
                    break  # If any part of the name matches, add the student and break the loop
            if row[2].lower().startswith(search_name.lower()):  # Check if the last name matches
                found_students.append(row)

    if found_students:
        for student in found_students:
            print(student)
    else:
        print("No student found with the given name.")

    input("Press Enter to return to the main menu...")

# Function to search student by ID Number
def search_student_by_id():
    search_id = input("Enter the ID Number of the student to search: ")
    found_students = []
    
    with open('students.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0].lower().startswith(search_id.lower()):
                found_students.append(row)
    if found_students:
        for student in found_students:
            print(student)
    else:
        print("No student found with the given ID Number.")

    input("Press Enter to return to the main menu...")

# Function to search course by course name
def search_course_by_name():
    search_name = input("Enter the name of the course to search: ")
    found_courses = []

    with open('courses.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[1].lower().startswith(search_name.lower()):
                found_courses.append(row)

    if found_courses:
        for course in found_courses:
            print(course)
    else:
        print("No course found with the given name.")

    input("Press Enter to return to the main menu...")

# Function to search course by course code
def search_course_by_code():
    search_code = input("Enter the Course Code of the course to search: ")
    found_courses = []
    
    with open('courses.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0].lower().startswith(search_code.lower()):
                found_courses.append(row)
    if found_courses:
        for course in found_courses:
            print(course)
    else:
        print("No course found with the given Course Code.")

    input("Press Enter to return to the main menu...")

# Main menu
def main_menu():
    while True:
        print("\n--- Student Information System ---")
        print("1. Add Student")
        print("2. Add Course")
        print("3. Delete Student")
        print("4. Delete Course")
        print("5. Edit Student")
        print("6. Edit Course")  
        print("7. List Students")
        print("8. List Courses")
        print("9. Search Student by Name")
        print("10. Search Student by ID")
        print("11. Search Course by Name")
        print("12. Search Course by Code")
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
            edit_course()  
        elif choice == '7':
            list_students()
        elif choice == '8':
            list_courses()
        elif choice == '9':
            search_student_by_name()
        elif choice == '10':
            search_student_by_id()
        elif choice == '11':
            search_course_by_name()
        elif choice == '12':
            search_course_by_code()
        elif choice == '0':
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
main_menu()
