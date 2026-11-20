class Library:
    def __init__(self):
        self.books = []
 
    def add_book(self, book):
        if book not in self.books:
            self.books.append(book)
            print("Book added successfully!")
        else:
            print("Book already exists!")
 
    def display(self):
        if self.books:
            print("\nAvailable Books:")
            for book in self.books:
                print(book)
        else:
            print("No books available!")
 
    def issue_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print("Book issued successfully!")
        else:
            print("Book not available!")
 
    def return_book(self, book):
        if book not in self.books:
            self.books.append(book)
            print("Book returned successfully!")
        else:
            print("Book is already available!")
 
 
l = Library()
 
while True:
    print("\n--- LIBRARY MANAGEMENT SYSTEM ---")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Exit")
 
    ch = int(input("Enter your choice: "))
 
    if ch == 1:
        book = input("Enter book name: ")
        l.add_book(book)
    elif ch == 2:
        l.display()
    elif ch == 3:
        book = input("Enter book name: ")
        l.issue_book(book)
    elif ch == 4:
        book = input("Enter book name: ")
        l.return_book(book)
    elif ch == 5:
        print("Exiting Library System!")
        break
    else:
        print("Invalid choice!")
