from datetime import date
 
attendance = {}
 
while True:
    print("\n----- ATTENDANCE TRACKER -----")
    print("1. Add Student")
    print("2. Mark Attendance")
    print("3. View Attendance")
    print("4. Exit")
 
    choice = input("Enter your choice: ")
 
    if choice == "1":
        roll = input("Enter Roll Number: ")
        name = input("Enter Student Name: ")
        attendance[roll] = {
            "name": name,
            "records": []
        }
        print("Student added successfully!")
 
    elif choice == "2":
        roll = input("Enter Roll Number: ")
        if roll in attendance:
            status = input("Enter P for Present or A for Absent: ")
            if status.upper() in ["P", "A"]:
                today = str(date.today())
                attendance[roll]["records"].append((today, status.upper()))
                print("Attendance marked successfully!")
            else:
                print("Invalid attendance status!")
        else:
            print("Student not found!")
 
    elif choice == "3":
        print("\n----- ATTENDANCE REPORT -----")
        for roll, student in attendance.items():
            records = student["records"]
            present = sum(1 for r in records if r[1] == "P")
            absent = sum(1 for r in records if r[1] == "A")
            total = present + absent
 
            if total > 0:
                percentage = (present / total) * 100
            else:
                percentage = 0
 
            print("\nRoll Number:", roll)
            print("Name:", student["name"])
            print("Present:", present)
            print("Absent:", absent)
            print("Attendance:", round(percentage, 2), "%")
 
    elif choice == "4":
        print("Exiting Attendance Tracker...")
        break
 
    else:
        print("Invalid choice!")
