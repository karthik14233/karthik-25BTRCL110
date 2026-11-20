contacts = []
 
while True:
    print("\n----- CONTACT BOOK -----")
    print("1. Add Contact")
    print("2. Display Contacts")
    print("3. Search Contact")
    print("4. Exit")
 
    choice = input("Enter your choice: ")
 
    if choice == "1":
        name = input("Enter Name: ")
        phone = input("Enter Phone Number: ")
        contact = {
            "name": name,
            "phone": phone
        }
        contacts.append(contact)
        print("Contact added successfully!")
 
    elif choice == "2":
        print("\n----- CONTACT LIST -----")
        for c in contacts:
            print("Name:", c["name"])
            print("Phone:", c["phone"])
 
    elif choice == "3":
        search = input("Enter name to search: ")
        found = False
        for c in contacts:
            if c["name"].lower() == search.lower():
                print("Contact Found!")
                print("Name:", c["name"])
                print("Phone:", c["phone"])
                found = True
                break
        if not found:
            print("Contact not found!")
 
    elif choice == "4":
        print("Exiting Contact Book...")
        break
 
    else:
        print("Invalid choice!")
