import csv
import tkinter as tk
from tkinter import messagebox

# Function to add a student
def add_student():
    # Create a new window for adding a student
    add_student_window = tk.Toplevel(root)
    add_student_window.title("Add Student")

    # Create input fields and labels
    label_id = tk.Label(add_student_window, text="ID:")
    label_id.grid(row=0, column=0)
    entry_id = tk.Entry(add_student_window)
    entry_id.grid(row=0, column=1)

    label_first_name = tk.Label(add_student_window, text="First Name:")
    label_first_name.grid(row=1, column=0)
    entry_first_name = tk.Entry(add_student_window)
    entry_first_name.grid(row=1, column=1)

    label_last_name = tk.Label(add_student_window, text="Last Name:")
    label_last_name.grid(row=2, column=0)
    entry_last_name = tk.Entry(add_student_window)
    entry_last_name.grid(row=2, column=1)

    label_gender = tk.Label(add_student_window, text="Gender:")
    label_gender.grid(row=3, column=0)
    entry_gender = tk.Entry(add_student_window)
    entry_gender.grid(row=3, column=1)

    label_year = tk.Label(add_student_window, text="Year:")
    label_year.grid(row=4, column=0)
    entry_year = tk.Entry(add_student_window)
    entry_year.grid(row=4, column=1)

    label_course = tk.Label(add_student_window, text="Course:")
    label_course.grid(row=5, column=0)
    entry_course = tk.Entry(add_student_window)
    entry_course.grid(row=5, column=1)

    # Function to handle the add student button click event
    def add_student_button_click():
        student_id = entry_id.get()

        # Check if student ID already exists
        with open('students.csv', 'r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == student_id:
                    messagebox.showerror("Error", "Student with ID Number already exists.")
                    return

        # Get input data from the remaining fields
        first_name = entry_first_name.get()
        last_name = entry_last_name.get()
        gender = entry_gender.get()
        year = entry_year.get()
        course = entry_course.get()

        # Append new student data to CSV
        with open('students.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([student_id, first_name, last_name, gender, year, course])

        messagebox.showinfo("Success", "Student added successfully.")
        add_student_window.destroy()

    # Create the add student button
    add_button = tk.Button(add_student_window, text="Add Student", command=add_student_button_click)
    add_button.grid(row=6, columnspan=2)

# Function to add a course
def add_course():
    # Create a new window for adding a course
    add_course_window = tk.Toplevel(root)
    add_course_window.title("Add Course")

    # Create input fields and labels
    label_id = tk.Label(add_course_window, text="Course Code:")
    label_id.grid(row=0, column=0)
    entry_id = tk.Entry(add_course_window)
    entry_id.grid(row=0, column=1)

    label_name = tk.Label(add_course_window, text="Name:")
    label_name.grid(row=1, column=0)
    entry_name = tk.Entry(add_course_window)
    entry_name.grid(row=1, column=1)

    label_code = tk.Label(add_course_window, text="College:")
    label_code.grid(row=2, column=0)
    entry_code = tk.Entry(add_course_window)
    entry_code.grid(row=2, column=1)

    # Function to handle the add course button click event
    def add_course_button_click():
        course_code = entry_id.get()

        # Check if course code already exists
        with open('courses.csv', 'r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == course_code:
                    messagebox.showerror("Error", "Course code already exists.")
                    return

        # Get input data from the remaining fields
        course_name = entry_name.get()
        course_college = entry_code.get()

        # Append new course data to CSV
        with open('courses.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([course_code, course_name, course_college])

        messagebox.showinfo("Success", "Course added successfully.")
        add_course_window.destroy()

    # Create the add course button
    add_button = tk.Button(add_course_window, text="Add Course", command=add_course_button_click)
    add_button.grid(row=3, columnspan=2)

# Function to delete a student
def delete_student():
    # Create a new window for deleting a student
    delete_student_window = tk.Toplevel(root)
    delete_student_window.title("Delete Student")

    # Create input fields and labels
    label_id = tk.Label(delete_student_window, text="ID:")
    label_id.grid(row=0, column=0)
    entry_id = tk.Entry(delete_student_window)
    entry_id.grid(row=0, column=1)

    # Function to handle the delete student button click event
    def delete_student_button_click():
        student_id = entry_id.get()
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
            messagebox.showinfo("Success", f"Deleted {rows_deleted} student(s) successfully.")
        else:
            messagebox.showinfo("Error", "Student not found.")
        delete_student_window.destroy()

    # Create the delete student button
    delete_button = tk.Button(delete_student_window, text="Delete Student", command=delete_student_button_click)
    delete_button.grid(row=1, columnspan=2)

# Function to delete a course
def delete_course():
    # Create a new window for deleting a course
    delete_course_window = tk.Toplevel(root)
    delete_course_window.title("Delete Course")

    # Create input fields and labels
    label_id = tk.Label(delete_course_window, text="Course Code:")
    label_id.grid(row=0, column=0)
    entry_id = tk.Entry(delete_course_window)
    entry_id.grid(row=0, column=1)

    # Function to handle the delete course button click event
    def delete_course_button_click():
        course_id = entry_id.get()
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
            messagebox.showinfo("Success", f"Deleted {rows_deleted} course(s) successfully.")
        else:
            messagebox.showinfo("Error", "Course not found.")
        delete_course_window.destroy()

    # Create the delete course button
    delete_button = tk.Button(delete_course_window, text="Delete Course", command=delete_course_button_click)
    delete_button.grid(row=1, columnspan=2)

# Function to edit a student
def edit_student():
    # Create a new window for editing a student
    edit_student_window = tk.Toplevel(root)
    edit_student_window.title("Edit Student")
    
    # Create input fields and labels
    label_id = tk.Label(edit_student_window, text="ID:")
    label_id.grid(row=0, column=0)
    entry_id = tk.Entry(edit_student_window)
    entry_id.grid(row=0, column=1)

    label_first_name = tk.Label(edit_student_window, text="First Name:")
    label_first_name.grid(row=1, column=0)
    entry_first_name = tk.Entry(edit_student_window)
    entry_first_name.grid(row=1, column=1)

    label_last_name = tk.Label(edit_student_window, text="Last Name:")
    label_last_name.grid(row=2, column=0)
    entry_last_name = tk.Entry(edit_student_window)
    entry_last_name.grid(row=2, column=1)

    label_gender = tk.Label(edit_student_window, text="Gender:")
    label_gender.grid(row=3, column=0)
    entry_gender = tk.Entry(edit_student_window)
    entry_gender.grid(row=3, column=1)

    label_year = tk.Label(edit_student_window, text="Year:")
    label_year.grid(row=4, column=0)
    entry_year = tk.Entry(edit_student_window)
    entry_year.grid(row=4, column=1)

    label_course = tk.Label(edit_student_window, text="Course:")
    label_course.grid(row=5, column=0)
    entry_course = tk.Entry(edit_student_window)
    entry_course.grid(row=5, column=1)

        # Function to handle the edit student button click event
    def edit_student_button_click():
        student_id = entry_id.get()
        with open('students.csv', 'r', newline='') as file:
            reader = csv.reader(file)
            rows = list(reader)
        for row in rows:
            if row[0] == student_id:
                row[1] = entry_first_name.get()
                row[2] = entry_last_name.get()
                row[3] = entry_gender.get()
                row[4] = entry_year.get()
                row[5] = entry_course.get()
                break
        with open('students.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)
        messagebox.showinfo("Success", "Student edited successfully.")
        edit_student_window.destroy()

    # Create the edit student button
    edit_button = tk.Button(edit_student_window, text="Edit Student", command=edit_student_button_click)
    edit_button.grid(row=6, columnspan=2)

# Function to list students
def list_students():
    # Create a new window for listing students
    list_students_window = tk.Toplevel(root)
    list_students_window.title("List Students")

    # Create a text widget to display the list
    text_widget = tk.Text(list_students_window)
    text_widget.grid()

    with open('students.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            text_widget.insert(tk.END, " ".join(row) + "\n")

    # Disable text widget editing
    text_widget.configure(state=tk.DISABLED)

# Function to list courses
def list_courses():
    # Create a new window for listing courses
    list_courses_window = tk.Toplevel(root)
    list_courses_window.title("List Courses")

    # Create a text widget to display the list
    text_widget = tk.Text(list_courses_window)
    text_widget.grid()

    with open('courses.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            text_widget.insert(tk.END, " ".join(row) + "\n")

    # Disable text widget editing
    text_widget.configure(state=tk.DISABLED)

# Function to search student by name
def search_student_by_name():
    # Create a new window for searching a student by name
    search_student_window = tk.Toplevel(root)
    search_student_window.title("Search Student by Name")

    # Create input fields and labels
    label_name = tk.Label(search_student_window, text="Name:")
    label_name.grid(row=0, column=0)
    entry_name = tk.Entry(search_student_window)
    entry_name.grid(row=0, column=1)

    # Function to handle the search student by name button click event
    def search_student_by_name_button_click():
        search_name = entry_name.get()
        found_students = []
        with open('students.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[1].lower() == search_name.lower():
                    found_students.append(row)
        if found_students:
            # Create a new window to display the search results
            search_results_window = tk.Toplevel(root)
            search_results_window.title("Search Results")

            # Create a text widget to display the search results
            text_widget = tk.Text(search_results_window)
            text_widget.grid()

            for student in found_students:
                text_widget.insert(tk.END, " ".join(student) + "\n")

            # Disable text widget editing
            text_widget.configure(state=tk.DISABLED)
        else:
            messagebox.showinfo("No Results", "No students found with the given name.")
        search_student_window.destroy()

        # Create the search student by name button
    search_button = tk.Button(search_student_window, text="Search", command=search_student_by_name_button_click)
    search_button.grid(row=1, columnspan=2)

# Function to search student by ID
def search_student_by_id():
    # Create a new window for searching a student by ID
    search_student_window = tk.Toplevel(root)
    search_student_window.title("Search Student by ID")

    # Create input fields and labels
    label_id = tk.Label(search_student_window, text="ID:")
    label_id.grid(row=0, column=0)
    entry_id = tk.Entry(search_student_window)
    entry_id.grid(row=0, column=1)

    # Function to handle the search student by ID button click event
    def search_student_by_id_button_click():
        search_id = entry_id.get()
        found_students = []
        with open('students.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == search_id:
                    found_students.append(row)
        if found_students:
            # Create a new window to display the search results
            search_results_window = tk.Toplevel(root)
            search_results_window.title("Search Results")

            # Create a text widget to display the search results
            text_widget = tk.Text(search_results_window)
            text_widget.grid()

            for student in found_students:
                text_widget.insert(tk.END, " ".join(student) + "\n")

            # Disable text widget editing
            text_widget.configure(state=tk.DISABLED)
        else:
            messagebox.showinfo("No Results", "No students found with the given ID.")
        search_student_window.destroy()

    # Create the search student by ID button
    search_button = tk.Button(search_student_window, text="Search", command=search_student_by_id_button_click)
    search_button.grid(row=1, columnspan=2)

# Create the main window
root = tk.Tk()
root.title("Student Information System")

# Create the main menu
main_menu_frame = tk.Frame(root)
main_menu_frame.pack(pady=20)

add_student_button = tk.Button(main_menu_frame, text="Add Student", command=add_student)
add_student_button.grid(row=0, column=0, padx=10)

add_course_button = tk.Button(main_menu_frame, text="Add Course", command=add_course)
add_course_button.grid(row=0, column=1, padx=10)

delete_student_button = tk.Button(main_menu_frame, text="Delete Student", command=delete_student)
delete_student_button.grid(row=0, column=2, padx=10)

delete_course_button = tk.Button(main_menu_frame, text="Delete Course", command=delete_course)
delete_course_button.grid(row=0, column=3, padx=10)

edit_student_button = tk.Button(main_menu_frame, text="Edit Student", command=edit_student)
edit_student_button.grid(row=1, column=0, padx=10, pady=10)

list_students_button = tk.Button(main_menu_frame, text="List Students", command=list_students)
list_students_button.grid(row=1, column=1, padx=10, pady=10)

list_courses_button = tk.Button(main_menu_frame, text="List Courses", command=list_courses)
list_courses_button.grid(row=1, column=2, padx=10, pady=10)

search_student_by_name_button = tk.Button(main_menu_frame, text="Search Student by Name", command=search_student_by_name)
search_student_by_name_button.grid(row=2, column=0, padx=10, pady=10)

search_student_by_id_button = tk.Button(main_menu_frame, text="Search Student by ID", command=search_student_by_id)
search_student_by_id_button.grid(row=2, column=1, padx=10, pady=10)

# Start the main event loop
root.mainloop()
