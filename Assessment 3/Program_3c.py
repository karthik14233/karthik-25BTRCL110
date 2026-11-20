numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
 
frequency = {}
 
for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1
 
print("\n----- FREQUENCY COUNT -----")
for num, count in frequency.items():
    print(num, ":", count)
