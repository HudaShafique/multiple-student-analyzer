students = []

t_students = int(input("How many students : "))

for i in range(t_students): #entity
    name = input(f"Enter Name of student {i + 1}: ")
    roll_no = input("Enter Roll no. : ")

    marks = []

    for j in range(5): #attributes
        mark = int(input(f"Enter marks {j + 1}: "))
        marks.append(mark)

    total = sum(marks)
    avg = total/len(marks)
    heighest = max(marks)
    lowest = min(marks)


    student = {
        "Name": name,
        "Roll no.": roll_no,
        "Marks": marks,
        "total": total,
        "average": avg,
        "heighest": heighest,
        "lowest": lowest
    }

    students.append(student)
    
print("Students data :\n ")

for student in students:
    print("Name:", student["Name"])
    print("Roll No:", student["Roll no."])
    print("Marks:", student["Marks"])
    print("Total :", student["total"])
    print("heighest :", student["heighest"])
    print("lowest :", student["lowest"])
    print("--" * 15)
