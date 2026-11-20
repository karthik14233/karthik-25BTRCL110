import csv
import os
 
filename = "students.csv"
 
# Create CSV file if it does not exist
if not os.path.exists(filename):
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Roll No", "Name", "Marks"])
 
while True:
    print("\n----- STUDENT DATA MANAGER -----")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Exit")
 
    choice = input("Enter your choice: ")
 
    if choice == "1":
        roll = input("Enter Roll Number: ")
        name = input("Enter Student Name: ")
        marks = input("Enter Marks: ")
 
        with open(filename, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([roll, name, marks])
        print("Student added successfully!")
 
    elif choice == "2":
        with open(filename, "r") as file:
            reader = csv.reader(file)
            print("\nRoll No\tName\tMarks")
            next(reader)
            for row in reader:
                print("\t".join(row))
 
    elif choice == "3":
        search_roll = input("Enter Roll Number to search: ")
        found = False
 
        with open(filename, "r") as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                if row[0] == search_roll:
                    print("\nStudent Found!")
                    print("Roll No:", row[0])
                    print("Name:", row[1])
                    print("Marks:", row[2])
                    found = True
                    break
 
        if not found:
            print("Student not found!")
 
    elif choice == "4":
        print("Exiting Student Manager...")
        break
 
    else:
        print("Invalid choice!")
