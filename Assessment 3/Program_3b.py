students = []
 
n = int(input("Enter number of students: "))
 
for i in range(n):
    print("\nEnter Student Details")
    name = input("Enter Name: ")
    m1 = int(input("Enter Subject 1 Marks: "))
    m2 = int(input("Enter Subject 2 Marks: "))
    m3 = int(input("Enter Subject 3 Marks: "))
 
    total = m1 + m2 + m3
    average = total / 3
 
    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 50:
        grade = "C"
    else:
        grade = "F"
 
    student = {
        "name": name,
        "total": total,
        "average": average,
        "grade": grade
    }
    students.append(student)
 
print("\n----- STUDENT RESULT -----")
for s in students:
    print("\nName:", s["name"])
    print("Total Marks:", s["total"])
    print("Average:", round(s["average"], 2))
    print("Grade:", s["grade"])
