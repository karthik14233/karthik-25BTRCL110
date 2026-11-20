try:
    filename = input("Enter log file name: ")
 
    with open(filename, "r") as file:
        print("\n----- LOG FILE CONTENTS -----")
        for line in file:
            print(line.strip())
 
except FileNotFoundError:
    print("Error: File not found!")
except Exception as e:
    print("Error:", e)
