import random
 
n = int(input("Enter number of dice rolls: "))
 
if n <= 0:
    print("Enter a positive number!")
else:
    for i in range(n):
        input("\nPress Enter to roll the dice: ")
        number = random.randint(1, 6)
        print("Dice Result:", number)
 
        if number == 6:
            print("Congratulations! You got 6!")
        elif number == 1:
            print("You got the lowest number!")
        else:
            print("Try again!")
