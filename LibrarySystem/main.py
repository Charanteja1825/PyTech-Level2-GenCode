from model import *

books = load_books()

while True:
    print("\n----- Library Management System -----")
    print("1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. Delete Book")
    print("5. View Available Books")
    print("6. Exit")

    choice = input("Enter choice: ").strip()

    if choice == "1":
        bid = input("Enter Book ID: ").strip()
        title = input("Enter Title: ").strip()

        if bid and title:
            books.append(Book(bid, title))
            save_all_books(books)
            print("Book Added Successfully.")
        else:
            print("All fields required.")

    elif choice == "2":
        bid = input("Enter Book ID: ").strip()
        found = False
        for b in books:
            if b.book_id == bid:
                found = True
                if not b.issued:
                    b.issued = True
                    print("Book Issued.")
                else:
                    print("Already Issued.")
                break
        if found:
            save_all_books(books)
        else:
            print("Book Not Found.")

    elif choice == "3":
        bid = input("Enter Book ID: ").strip()
        found = False
        for b in books:
            if b.book_id == bid:
                found = True
                if b.issued:
                    b.issued = False
                    print("Book Returned.")
                else:
                    print("Book was not issued.")
                break
        if found:
            save_all_books(books)
        else:
            print("Book Not Found.")

    elif choice == "4":
        bid = input("Enter Book ID: ").strip()
        new_books = [b for b in books if b.book_id != bid]

        if len(new_books) != len(books):
            books = new_books
            save_all_books(books)
            print("Deleted Successfully.")
        else:
            print("Book Not Found.")

    elif choice == "5":
        available = [b for b in books if not b.issued]
        if not available:
            print("No available books.")
        else:
            for b in available:
                print(f"ID: {b.book_id}, Title: {b.title}")

    elif choice == "6":
        print("Exiting...")
        break

    else:
        print("Invalid choice. Try again.")