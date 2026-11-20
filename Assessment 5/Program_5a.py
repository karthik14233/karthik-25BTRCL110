class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
 
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Amount deposited successfully!")
        else:
            print("Invalid amount!")
 
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print("Amount withdrawn successfully!")
        else:
            print("Insufficient balance or invalid amount!")
 
    def display(self):
        print("\nAccount Holder:", self.name)
        print("Available Balance:", self.balance)
 
 
name = input("Enter account holder name: ")
balance = float(input("Enter initial balance: "))
 
a = BankAccount(name, balance)
 
while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Display Balance")
    print("4. Exit")
 
    ch = int(input("Enter your choice: "))
 
    if ch == 1:
        amount = float(input("Enter deposit amount: "))
        a.deposit(amount)
    elif ch == 2:
        amount = float(input("Enter withdrawal amount: "))
        a.withdraw(amount)
    elif ch == 3:
        a.display()
    elif ch == 4:
        print("Thank you for using our bank!")
        break
    else:
        print("Invalid choice!")
