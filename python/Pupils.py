# Create a dictionary to store students name and their subjects
students = {}

# Get the number of students
number= int(input("Write number of students: "))

# Get every student name and subject
for i in range(number):
    name_stud = input(f"Name of {i + 1} student: ")
    subjects = input(f"Subjects of {i + 1} student: ").split()
    students[name_stud] = subjects

# Function to show all students and their subjects, sorted in descending order by name
def show_all():
    for student in sorted(students.keys(), reverse=True):
        print(f"{student}: {students[student]}")

# This function is  to get subjects for a specific student
def student_for_sub(name_stud):
    if name_stud in students:
        return students[name_stud]
    else:
        return "There are no students with this name."

# This function to get students studying a specific subject
def student_sub(subject):
    matching_students = [name for name, subjects in students.items() if subject in subjects]
    if matching_students:
        return matching_students
    else:
        return "There are no matching students."

# Example 
print("\nStudents and Subjects:")
show_all()

# Get subjects for a specific student
name = input("\nEnter a student's name to find their subjects: ")
print(student_for_sub(name))

# Get students studying a specific subject
subject = input("\nEnter a subject to find students studying it: ")
print(student_sub(subject))
