import csv
 
filename = "payroll.csv"
 
with open(filename, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([
        "Employee ID",
        "Name",
        "Basic Salary",
        "HRA",
        "DA",
        "PF",
        "Net Salary"
    ])
 
    n = int(input("Enter number of employees: "))
 
    for i in range(n):
        print("\nEnter Employee Details")
        emp_id = input("Employee ID: ")
        name = input("Employee Name: ")
        basic = float(input("Basic Salary: "))
 
        hra = basic * 0.20
        da = basic * 0.10
        pf = basic * 0.12
 
        gross = basic + hra + da
        net = gross - pf
 
        writer.writerow([emp_id, name, basic, hra, da, pf, net])
 
        print("\nEmployee Salary Details")
        print("HRA:", hra)
        print("DA:", da)
        print("PF:", pf)
        print("Gross Salary:", gross)
        print("Net Salary:", net)
 
print("\nPayroll data saved successfully!")
