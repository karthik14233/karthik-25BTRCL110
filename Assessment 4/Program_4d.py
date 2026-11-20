import json
 
try:
    filename = input("Enter JSON file name: ")
 
    with open(filename, "r") as file:
        logs = json.load(file)
 
    info = 0
    warning = 0
    error = 0
 
    print("\n----- LOG ANALYSIS REPORT -----")
 
    for log in logs:
        level = log["level"]
        if level == "INFO":
            info += 1
        elif level == "WARNING":
            warning += 1
        elif level == "ERROR":
            error += 1
 
    print("Total Log Records:", len(logs))
    print("INFO Messages:", info)
    print("WARNING Messages:", warning)
    print("ERROR Messages:", error)
 
    print("\n----- ERROR MESSAGES -----")
    for log in logs:
        if log["level"] == "ERROR":
            print(log["message"])
 
except FileNotFoundError:
    print("Error: JSON file not found!")
except json.JSONDecodeError:
    print("Error: Invalid JSON format!")
except KeyError:
    print("Error: Required log field is missing!")
finally:
    print("\nLog analysis completed.")
