print("----- UNIT CONVERTER -----")
print("1. Kilometers to Miles")
print("2. Miles to Kilometers")
print("3. Celsius to Fahrenheit")
print("4. Fahrenheit to Celsius")
print("5. Kilograms to Pounds")
print("6. Pounds to Kilograms")
 
choice = int(input("Enter your choice: "))
value = float(input("Enter the value: "))
 
if choice == 1:
    result = value * 0.621371
    print(value, "km =", result, "miles")
elif choice == 2:
    result = value * 1.60934
    print(value, "miles =", result, "km")
elif choice == 3:
    result = (value * 9 / 5) + 32
    print(value, "°C =", result, "°F")
elif choice == 4:
    result = (value - 32) * 5 / 9
    print(value, "°F =", result, "°C")
elif choice == 5:
    result = value * 2.20462
    print(value, "kg =", result, "pounds")
elif choice == 6:
    result = value / 2.20462
    print(value, "pounds =", result, "kg")
else:
    print("Invalid choice.")
