import json
from datetime import datetime, timedelta

BOOK_FILE = 'books.json'
STUDENT_FILE = 'issued.json'

def load_data(file):
    try:
        with open(file, 'r') as f:
            return json.load(f)
    except:
        return {}

def save_data(file, data):
    with open(file, 'w') as f:
        json.dump(data, f, indent=4)

def add_book():
    books = load_data(BOOK_FILE)
    book_id = input("Enter book ID: ")
    title = input("Enter book title: ")
    if book_id in books:
        print(f"Book ID '{book_id}' already exists.")
    else:
        books[book_id] = title
        save_data(BOOK_FILE, books)
        print(f"Book '{title}' added successfully.")

def remove_book():
    books = load_data(BOOK_FILE)
    book_id = input("Enter book ID to remove: ")
    if book_id in books:
        removed_title = books[book_id]
        del books[book_id]
        save_data(BOOK_FILE, books)
        print(f"Book '{removed_title}' removed successfully.")
    else:
        print("Book not found.")

def issue_book():
    issued = load_data(STUDENT_FILE)
    books = load_data(BOOK_FILE)
    student = input("Enter student name: ")
    book_id = input("Enter book ID to issue: ")

    if book_id in books:
        for record in issued.values():
            if record["book_id"] == book_id:
                print("Book already issued to another student.")
                return
        due_date = (datetime.now() + timedelta(days=7)).strftime('%Y-%m-%d')
        issued[student] = {"book_id": book_id, "due_date": due_date}
        save_data(STUDENT_FILE, issued)
        print(f"Issued '{books[book_id]}' to {student}, due by {due_date}.")
    else:
        print("Book not available.")

def return_book():
    issued = load_data(STUDENT_FILE)
    books = load_data(BOOK_FILE)
    student = input("Enter student name: ")

    if student in issued:
        book_id = issued[student]["book_id"]
        title = books.get(book_id, "Unknown")
        due = datetime.strptime(issued[student]["due_date"], '%Y-%m-%d')
        today = datetime.now()
        fine = (today - due).days * 5 if today > due else 0
        del issued[student]
        save_data(STUDENT_FILE, issued)
        print(f"Book '{title}' returned. Fine: ₹{fine}")
    else:
        print("No book issued to this student.")

def main():
    while True:
        print("\n------ Library Menu ------")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            add_book()
        elif choice == '2':
            remove_book()
        elif choice == '3':
            issue_book()
        elif choice == '4':
            return_book()
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

main()
