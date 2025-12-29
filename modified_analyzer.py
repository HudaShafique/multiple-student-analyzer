# --------------------------
# Function 1: Input student details
# --------------------------
def input_student_details(student_num):
    """Take name, roll no., and marks for a single student."""
    print(f"\nEntering data for student {student_num}")
    name = input("Enter Name: ")
    roll_no = input("Enter Roll No.: ")

    marks = []
    for i in range(5):
        mark = int(input(f"Enter marks {i + 1}: "))
        marks.append(mark)

    return name, roll_no, marks

# --------------------------
# Function 2: Calculate stats
# --------------------------
def calculate_stats(marks):
    """Calculate total, average, highest, and lowest marks."""
    total = sum(marks)
    average = total / len(marks)
    highest = max(marks)
    lowest = min(marks)
    return total, average, highest, lowest

# --------------------------
# Function 3: Assign grade
# --------------------------
def assign_grade(average):
    """Return grade and remark based on average."""
    if average >= 90:
        return "A", "Excellent"
    elif average >= 80:
        return "B", "Good"
    elif average >= 60:
        return "C", "Fair"
    else:
        return "D", "Needs Improvement"

# --------------------------
# Function 4: Print student report
# --------------------------
def print_student_report(student):
    """Print the details of a single student."""
    print("\n-----------------------------")
    print(f"Name: {student['Name']}")
    print(f"Roll No: {student['Roll No']}")
    print(f"Marks: {student['Marks']}")
    print(f"Total: {student['Total']}")
    print(f"Average: {student['Average']:.2f}")
    print(f"Highest: {student['Highest']}")
    print(f"Lowest: {student['Lowest']}")
    print(f"Grade: {student['Grade']}")
    print(f"Remark: {student['Remark']}")
    print("-----------------------------")

# --------------------------
# Main Program
# --------------------------
students = []

t_students = int(input("How many students: "))

for i in range(1, t_students + 1):
    name, roll_no, marks = input_student_details(i)
    total, average, highest, lowest = calculate_stats(marks)
    grade, remark = assign_grade(average)

    student = {
        "Name": name,
        "Roll No": roll_no,
        "Marks": marks,
        "Total": total,
        "Average": average,
        "Highest": highest,
        "Lowest": lowest,
        "Grade": grade,
        "Remark": remark
    }

    students.append(student)

# Print reports for all students
print("\n==== Students Data ====")
for student in students:
    print_student_report(student)
