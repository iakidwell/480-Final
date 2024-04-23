iakidwell
iakidwell
Online
SpaghettiCats, dusty_ally

iakidwell — 04/21/2024 3:30 PM
awesome thank you
i'm so relieved to see the grading schema lol
dusty_ally — 04/21/2024 3:30 PM
Yeah the matrial is  too vast
iakidwell — 04/21/2024 3:30 PM
he isn't doing a great job of explaining it or contextualizing it
but that's okay
i am listening on 1.5x speed so maybe i'm loosing something lol
dusty_ally — 04/21/2024 3:30 PM
i guess preparing the homework and midterm exam would put us in a good shape
iakidwell — 04/21/2024 3:35 PM
i might use some PTO this week to make time to work on this final. but hopefully that can be avoided
dusty_ally — Yesterday at 11:42 AM
guys any idea on how to connect sql and python
i am trying to use vs code but failing to connect to the database
iakidwell — Yesterday at 12:42 PM
i can look into it slightyl later this afternoon
iakidwell — Yesterday at 4:18 PM
do we have a repository going?
iakidwell — Yesterday at 4:36 PM
I have an executive decision for this project if you guys are fine with it
we should use SQLite and avoid the server/client model and any complications that come with it
SQLite is preinstalled with python as well
I am building out the basics of the menu system. I will then turn to getting SQLite and the database set up
from there is should be pretty easy to divide and conquer: we can each take some functionalities off of the project rubrick and complete them
iakidwell — Yesterday at 5:10 PM
ok stepping away from the computer for now but I wanted to update you guys on progress. I made another repository because I didn't know where to put what I was working on otherwise. here is the link:
https://github.com/iakidwell/480-Final
GitHub
GitHub - iakidwell/480-Final: Application for the 480 Final project
Application for the 480 Final project. Contribute to iakidwell/480-Final development by creating an account on GitHub.
GitHub - iakidwell/480-Final: Application for the 480 Final project
Here is what I did:
create the loop and menu items for the librarians and clients (w/o functionality obviously)
implement SQLite and run our DDL script from phase 2 of the project. (see: createDB.py)
Remember: SQLite does not use the Server-Client model for database management, which means we side step any networking problems. Just a heads up.
When you guys get a chance could you review and give thoughts? I have a lot of time tomorrow to work on this project.
thank u!
dusty_ally — Yesterday at 8:08 PM
Yeah I already Uploaded the previous files
dusty_ally — Yesterday at 8:09 PM
so can we access the git with SQlite
dusty_ally — Yesterday at 9:24 PM
Alright I just forked
and connected to Vscode
I didn't knew Sqlite is this easy
But i have one question we have to make ourr project work according to PostgreSql right
Does Sqlite and Postgre both the same syntax ??
iakidwell — Yesterday at 9:47 PM
good catch
no we do not. postgres is not an explicit requirement according to the project page on the website
SQLite has very similar syntax to postgres with some small differences
how should we divide up the labor for this project?
i took work off tomorrow but i also need to prepare for the final
dusty_ally — Yesterday at 9:53 PM
I just the code
Of the library update delete methods
Good work
I’ll try working on the backend
iakidwell — Yesterday at 10:04 PM
okay. i will be very vocal about when i'm doing tasks so we don't double do work
dusty_ally — Yesterday at 10:14 PM
So when u work and pushing it to git comment your name and changes u pushed
So it would be easy for us to figure out if any mistake occurs to fix the particular problem
iakidwell — Yesterday at 10:15 PM
i am a total git noob
so if you have any more guidance i will happily adhere
dusty_ally — Yesterday at 10:16 PM
Ok I’ll send you some git commands for pushing and pulling
iakidwell — Yesterday at 10:16 PM
thank you!
dusty_ally — Today at 3:42 AM
Guys I made some changes to the code and push it to the git please check
It’s working for now
dusty_ally — Today at 9:00 AM
And guys before u start working on the don’t forget to pull the data from git which I worked on. Then don’t forget to push the data to git after u work
iakidwell — Today at 10:39 AM
how is that done?
dusty_ally — Today at 10:52 AM
Do you work on vs code ?
iakidwell — Today at 10:52 AM
yes
dusty_ally — Today at 10:53 AM
Alright then it is easy
iakidwell — Today at 11:05 AM
i'm working on the librarian functionalities rn
dusty_ally — Today at 11:06 AM
Did u pull the data from git ?
iakidwell — Today at 11:06 AM
no. how is that done?
what do you mean by data? total noob moment
dusty_ally — Today at 11:06 AM
So ur working on vs code u have to connect to git repository and pull the data
I’ll send one example video
iakidwell — Today at 11:07 AM
thank you!
dusty_ally — Today at 11:09 AM
https://youtu.be/9oKFPTtyHZg?si=ND7VZ4RCsCV6OY-D
YouTube
Christian Nwamba
Push and Pull to GitHub with VS Code
Image
This will help you
dusty_ally — Today at 11:10 AM
I worked on the library functionalities yesterday
iakidwell — Today at 11:10 AM
oh!
dusty_ally — Today at 11:10 AM
So I uploaded the work to git
iakidwell — Today at 11:10 AM
when you say the data, what are you referring to?
the work you did?
dusty_ally — Today at 11:10 AM
And you pull the work I did and can work on it
dusty_ally — Today at 11:10 AM
Yes 😅
iakidwell — Today at 11:10 AM
ahhhh awesome
lololol
dusty_ally — Today at 11:10 AM
😅
iakidwell — Today at 11:11 AM
i'm gonna be a SWE in no time
ok what were you able to knock out?
also are either of you going to class in person today? i am
iakidwell — Today at 11:20 AM
i'm so sorry i'm not seeing where your work is on the github. when i pull nothing shows up.
are we talking about the same repo? "480-Final"
dusty_ally — Today at 11:22 AM
Yes one u created
iakidwell — Today at 11:23 AM
where on the github repository can i go to find your data?
dusty_ally — Today at 11:23 AM
If your not to pull the data
Open git and then download the files
And also can work it
iakidwell — Today at 11:24 AM
the files only contain the code i wrote yesterday
dusty_ally — Today at 11:25 AM
How many lines is the code?
It was somewhere around 420
iakidwell — Today at 11:25 AM
main.py is 168
dusty_ally — Today at 11:25 AM
Damn 🤯
iakidwell — Today at 11:25 AM
yeah i don't see your stuff at all
ok so i'm not crazy lol
dusty_ally — Today at 11:25 AM
Just a sec
iakidwell — Today at 11:26 AM
kk
dusty_ally — Today at 11:26 AM
I’ll try sending here
iakidwell — Today at 11:28 AM
do you guys have any idea of how we should divide up the rest of the work? it seems super manageable if we're all accountable for a smaller chunk to implement
dusty_ally — Today at 11:28 AM
import sqlite3
import createDB
from datetime import datetime

def librarian_menu():
    print("Librarian Menu:")
    print("1. Manage Documents")
    print("2. Manage Librarians")
    print("3. Client Management")
    print("4. View Lent Out Documents")
    print("5. Exit")
    choice = input("Enter your choice: ")
    return choice

def manage_librarians_menu():
    print("Manage Librarians:")
    print("1. Add New Librarian")
    print("2. Update Librarian Details")
    print("3. Go Back to Librarian Menu")
    choice = input("Enter your choice: ")
    return choice

def add_librarian():
    print("Add New Librarian:")
    ssn = input("Enter SSN: ")
    name = input("Enter Name: ")
    email = input("Enter Email: ")
    salary = input("Enter Salary: ")
    
    with sqlite3.connect('library.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT SSN FROM librarian WHERE SSN = ?", (ssn,))
        if cursor.fetchone():
            print("A librarian with this SSN already exists.")
            return
        try:
            cursor.execute("INSERT INTO librarian (SSN, name, email, salary) VALUES (?, ?, ?, ?)",
                           (ssn, name, email, salary))
            conn.commit()
            print("Librarian added successfully.")
        except sqlite3.IntegrityError as e:
            print(f"Failed to add the librarian. Error: {e}")

def update_librarian():
    ssn = input("Enter SSN of the librarian to update: ")
    print("Update Librarian Details:")
    new_name = input("Enter new name (leave blank to keep current): ")
    new_email = input("Enter new email (leave blank to keep current): ")
    new_salary = input("Enter new salary (leave blank to keep current): ")
    
    with sqlite3.connect('library.db') as conn:
        cursor = conn.cursor()
        updates = []
        params = []
        if new_name:
            updates.append("name = ?")
            params.append(new_name)
        if new_email:
            updates.append("email = ?")
            params.append(new_email)
        if new_salary:
            updates.append("salary = ?")
            params.append(new_salary)
        params.append(ssn)
        update_query = f"UPDATE librarian SET {', '.join(updates)} WHERE SSN = ?"
        cursor.execute(update_query, params)
        if cursor.rowcount:
            conn.commit()
            print("Librarian updated successfully.")
        else:
            print("No librarian found with the given SSN or no updates made.")

def manage_documents_menu():
    print("Manage Documents:")
    print("1. Insert New Document")
    print("2. Update Document")
    print("3. Delete Document Copy")
    print("4. Go Back to Librarian Menu")
    choice = input("Enter your choice: ")
    return choice

def insert_new_book():
    print("Insert New Book:")
    isbn = input("Enter ISBN: ")
    title = input("Enter title: ")
    publisher = input("Enter publisher: ")
    edition = input("Enter edition: ")
    num_pages = input("Enter number of pages: ")
    authors = input("Enter authors (comma-separated): ").split(',')

    with sqlite3.connect('library.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT isbn FROM book WHERE isbn = ?", (isbn,))
        if cursor.fetchone():
            print("A book with this ISBN already exists.")
            return
        try:
            cursor.execute("INSERT INTO book (isbn, publisher, title, edition, num_pages) VALUES (?, ?, ?, ?, ?)",
                           (isbn, publisher, title, edition, num_pages))
            for author in authors:
... (357 lines left)
Collapse
main.py
20 KB
dusty_ally — Today at 11:28 AM
I can see on git
For now u can work on this
iakidwell — Today at 11:29 AM
oh this is great
dusty_ally — Today at 11:29 AM
In the evening I can tell u detailly
iakidwell — Today at 11:29 AM
i see you have a handle on SQLite
yeah ill push your work
﻿
import sqlite3
import createDB
from datetime import datetime

def librarian_menu():
    print("Librarian Menu:")
    print("1. Manage Documents")
    print("2. Manage Librarians")
    print("3. Client Management")
    print("4. View Lent Out Documents")
    print("5. Exit")
    choice = input("Enter your choice: ")
    return choice

def manage_librarians_menu():
    print("Manage Librarians:")
    print("1. Add New Librarian")
    print("2. Update Librarian Details")
    print("3. Go Back to Librarian Menu")
    choice = input("Enter your choice: ")
    return choice

def add_librarian():
    print("Add New Librarian:")
    ssn = input("Enter SSN: ")
    name = input("Enter Name: ")
    email = input("Enter Email: ")
    salary = input("Enter Salary: ")
    
    with sqlite3.connect('library.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT SSN FROM librarian WHERE SSN = ?", (ssn,))
        if cursor.fetchone():
            print("A librarian with this SSN already exists.")
            return
        try:
            cursor.execute("INSERT INTO librarian (SSN, name, email, salary) VALUES (?, ?, ?, ?)",
                           (ssn, name, email, salary))
            conn.commit()
            print("Librarian added successfully.")
        except sqlite3.IntegrityError as e:
            print(f"Failed to add the librarian. Error: {e}")

def update_librarian():
    ssn = input("Enter SSN of the librarian to update: ")
    print("Update Librarian Details:")
    new_name = input("Enter new name (leave blank to keep current): ")
    new_email = input("Enter new email (leave blank to keep current): ")
    new_salary = input("Enter new salary (leave blank to keep current): ")
    
    with sqlite3.connect('library.db') as conn:
        cursor = conn.cursor()
        updates = []
        params = []
        if new_name:
            updates.append("name = ?")
            params.append(new_name)
        if new_email:
            updates.append("email = ?")
            params.append(new_email)
        if new_salary:
            updates.append("salary = ?")
            params.append(new_salary)
        params.append(ssn)
        update_query = f"UPDATE librarian SET {', '.join(updates)} WHERE SSN = ?"
        cursor.execute(update_query, params)
        if cursor.rowcount:
            conn.commit()
            print("Librarian updated successfully.")
        else:
            print("No librarian found with the given SSN or no updates made.")

def manage_documents_menu():
    print("Manage Documents:")
    print("1. Insert New Document")
    print("2. Update Document")
    print("3. Delete Document Copy")
    print("4. Go Back to Librarian Menu")
    choice = input("Enter your choice: ")
    return choice

def insert_new_book():
    print("Insert New Book:")
    isbn = input("Enter ISBN: ")
    title = input("Enter title: ")
    publisher = input("Enter publisher: ")
    edition = input("Enter edition: ")
    num_pages = input("Enter number of pages: ")
    authors = input("Enter authors (comma-separated): ").split(',')

    with sqlite3.connect('library.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT isbn FROM book WHERE isbn = ?", (isbn,))
        if cursor.fetchone():
            print("A book with this ISBN already exists.")
            return
        try:
            cursor.execute("INSERT INTO book (isbn, publisher, title, edition, num_pages) VALUES (?, ?, ?, ?, ?)",
                           (isbn, publisher, title, edition, num_pages))
            for author in authors:
                cursor.execute("INSERT INTO book_authors (isbn, author) VALUES (?, ?)", (isbn, author))
            conn.commit()
            print("Book inserted successfully.")
        except sqlite3.IntegrityError as e:
            print(f"Failed to insert the book. Error: {e}")



def update_document():
    isbn = input("Enter the ISBN of the document to update: ")
    print("What would you like to update?")
    print("1. Title")
    print("2. Publisher")
    print("3. Number of Pages")
    update_choice = input("Enter your choice: ")

    with sqlite3.connect('library.db') as conn:
        cursor = conn.cursor()
        if update_choice == "1":
            new_title = input("Enter the new title: ")
            cursor.execute("UPDATE book SET title = ? WHERE isbn = ?", (new_title, isbn))
        elif update_choice == "2":
            new_publisher = input("Enter the new publisher: ")
            cursor.execute("UPDATE book SET publisher = ? WHERE isbn = ?", (new_publisher, isbn))
        elif update_choice == "3":
            new_num_pages = input("Enter the new number of pages: ")
            if new_num_pages.isdigit():  # Ensure that the input is a number
                cursor.execute("UPDATE book SET num_pages = ? WHERE isbn = ?", (int(new_num_pages), isbn))
            else:
                print("Invalid input for number of pages. It must be a number.")
                return

        if cursor.rowcount == 0:
            print("No document found with the given ISBN or update failed.")
        else:
            conn.commit()
            print("Document updated successfully.")

def return_document():
    email = input("Enter your email: ")
    isbn = input("Enter the ISBN of the document to return: ")
    with sqlite3.connect('library.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT due_date FROM client_loans WHERE isbn = ? AND email = ?", (isbn, email))
        result = cursor.fetchone()
        if result:
            due_date = datetime.strptime(result[0], '%Y-%m-%d')
            return_date = datetime.now()
            overdue_days = max(0, (return_date - due_date).days)
            if overdue_days > 0:
                overdue_fee = 5 * overdue_days
                cursor.execute("UPDATE client SET overdue_fees = overdue_fees + ? WHERE email = ?", (overdue_fee, email))
                print(f"Document is overdue. Fee charged: ${overdue_fee:.2f}")
            cursor.execute("UPDATE document SET on_loan = 0 WHERE isbn = ?", (isbn,))
            conn.commit()
            print("Document returned successfully.")
        else:
            print("No loan record found for this document and client.")



def update_client_information():
    email = input("Enter the client's email to update: ")
    print("Select an option to update:")
    print("1. Update Name")
    print("2. Update/Add Address")
    print("3. Update/Add Credit Card")
    choice = input("Enter your choice: ")

    with sqlite3.connect('library.db') as conn:
        cursor = conn.cursor()
        if choice == '1':
            new_name = input("Enter the new name for the client: ")
            cursor.execute("UPDATE client SET name = ? WHERE email = ?", (new_name, email))
            if cursor.rowcount:
                conn.commit()
                print("Client's name updated successfully.")
            else:
                print("No client found with the given email or no updates made.")
        elif choice == '2':
            new_address = input("Enter new or additional address: ")
            cursor.execute("INSERT INTO addresses (client_email, address) VALUES (?, ?)", (email, new_address))
            if cursor.rowcount:
                conn.commit()
                print("Address updated/added successfully.")
            else:
                print("Failed to update/add address.")
        elif choice == '3':
            new_card = input("Enter new or additional credit card number: ")
            print("Available addresses:")
            cursor.execute("SELECT id, address FROM addresses WHERE client_email = ?", (email,))
            addresses = cursor.fetchall()
            for addr in addresses:
                print(f"{addr[0]}: {addr[1]}")
            address_id = input("Select address ID for this card: ")
            cursor.execute("INSERT INTO credit_cards (client_email, credit_card_number, address_id) VALUES (?, ?, ?)", (email, new_card, address_id))
            if cursor.rowcount:
                conn.commit()
                print("Credit card updated/added successfully.")
            else:
                print("Failed to update/add credit card.")
        else:
            print("Invalid choice. Please try again.")



def register_new_client():
    print("Register New Client:")
    name = input("Enter client's name: ")
    email = input("Enter client's email: ")
    addresses = input("Enter client's addresses (comma-separated): ").split(',')
    payment_methods = input("Enter payment card numbers (comma-separated): ").split(',')

    with sqlite3.connect('library.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT email FROM client WHERE email = ?", (email,))
        if cursor.fetchone():
            print("A client with this email already exists.")
            return
        try:
            cursor.execute("INSERT INTO client (email, name) VALUES (?, ?)", (email, name))
            address_ids = []
            for address in addresses:
                cursor.execute("INSERT INTO addresses (client_email, address) VALUES (?, ?)", (email, address))
                address_ids.append(cursor.lastrowid)
            for card_number in payment_methods:
                address_id = address_ids[min(len(address_ids) - 1, payment_methods.index(card_number))]  # Associate with corresponding address or last one
                cursor.execute("INSERT INTO credit_cards (client_email, credit_card_number, address_id) VALUES (?, ?, ?)", (email, card_number, address_id))
            conn.commit()
            print("Client registered successfully with multiple addresses and payment methods.")
        except sqlite3.IntegrityError as e:
            print(f"Failed to register client. Error: {e}")


def delete_client():
    email = input("Enter the client's email to delete: ")
    with sqlite3.connect('library.db') as conn:
        cursor = conn.cursor()
        # Check if client has any borrowed documents before deleting
        cursor.execute("SELECT * FROM client_loans WHERE email = ?", (email,))
        if cursor.fetchall():
            print("Cannot delete client because they have borrowed documents.")
            return
        cursor.execute("DELETE FROM client WHERE email = ?", (email,))
        if cursor.rowcount:
            conn.commit()
            print("Client deleted successfully.")
        else:
            print("No client found with the given email.")

def search_documents_by_title():
    title_search = input("Enter the title to search for: ")
    
    with sqlite3.connect('library.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT isbn, title, publisher FROM book WHERE title LIKE ?", ('%' + title_search + '%',))
        books = cursor.fetchall()
        if books:
            for book in books:
                print(f"ISBN: {book[0]}, Title: {book[1]}, Publisher: {book[2]}")
        else:
            print("No books found with the given title.")

def search_documents_advanced():
    print("Advanced Document Search:")
    search_type = input("Search by (title/author/isbn/publisher/year): ").lower()
    search_query = input("Enter search value: ")

    with sqlite3.connect('library.db') as conn:
        cursor = conn.cursor()
        query = {
            'title': "SELECT isbn, title, publisher FROM book WHERE title LIKE ?",
            'author': "SELECT b.isbn, b.title, b.publisher FROM book b JOIN book_authors ba ON b.isbn = ba.isbn WHERE ba.author LIKE ?",
            'isbn': "SELECT isbn, title, publisher FROM book WHERE isbn = ?",
            'publisher': "SELECT isbn, title, publisher FROM book WHERE publisher LIKE ?",
            'year': "SELECT isbn, title, publisher FROM book WHERE year = ?"
        }
        execute_query = query.get(search_type, "SELECT isbn, title, publisher FROM book WHERE title LIKE ?")  # Default to title search
        cursor.execute(execute_query, ('%' + search_query + '%',) if search_type != 'isbn' and search_type != 'year' else (search_query,))
        books = cursor.fetchall()
        if books:
            for book in books:
                print(f"ISBN: {book[0]}, Title: {book[1]}, Publisher: {book[2]}")
        else:
            print("No books found matching the criteria.")

def delete_document_copy():
    copy_number = input("Enter the copy number of the document to delete: ")
    with sqlite3.connect('library.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT on_loan FROM document WHERE copy_number = ?", (copy_number,))
        result = cursor.fetchone()
        if result and not result[0]:  # Checking if the document is not on loan
            cursor.execute("DELETE FROM document WHERE copy_number = ?", (copy_number,))
            conn.commit()
            print("Document copy deleted successfully.")
        elif result:
            print("Cannot delete the document copy as it is currently on loan.")
        else:
            print("Document copy not found.")

def view_lent_out_documents():
    with sqlite3.connect('library.db') as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT cl.email, b.title, cl.due_date
            FROM client_loans cl
            JOIN book b ON cl.isbn = b.isbn
            WHERE cl.returned = 0  -- Assuming there is a 'returned' flag in your client_loans table
        """)
        loans = cursor.fetchall()
        if loans:
            print("Currently Lent Out Documents:")
            for loan in loans:
                print(f"Client Email: {loan[0]}, Title: {loan[1]}, Due Date: {loan[2]}")
        else:
            print("No documents are currently lent out.")

def borrow_document():
    email = input("Enter your email: ")
    isbn = input("Enter the ISBN of the book to borrow: ")
    with sqlite3.connect('library.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT on_loan FROM document WHERE isbn = ?", (isbn,))
        document = cursor.fetchone()
        if document and not document[0]:  # Check if the document is not currently on loan
            cursor.execute("UPDATE document SET on_loan = 1 WHERE isbn = ?", (isbn,))
            conn.commit()
            print("Document successfully borrowed.")
        else:
            print("This document is currently unavailable.")


def client_management_menu():
    print("Client Management:")
    print("1. Register New Client")
    print("2. Update Client Information")
    print("3. Delete Client")
    print("4. Go Back to Librarian Menu")
    choice = input("Enter your choice: ")
    return choice

def client_menu():
    print("Client Menu:")
    print("1. Search for Documents")
    print("2. Borrow a Document")
    print("3. Return a Document")
    print("4. Pay Overdue Fees")
    print("5. Manage Payment Methods")
    print("6. Exit")
    choice = input("Enter your choice: ")
    return choice

def search_documents_menu():
    print("Search for Documents:")
    print("1. Search by Title")
    print("2. Search by Author")
    print("3. Search by ISBN")
    print("4. Search by Publisher")
    print("5. Search by Edition")
    print("6. Search by Year")
    print("7. Go Back to Client Menu")
    choice = input("Enter your choice: ")
    return choice

def manage_payment_methods_menu():
    print("Manage Payment Methods:")
    print("1. Add Payment Method")
    print("2. Delete Payment Method")
    print("3. Go Back to Client Menu")
    choice = input("Enter your choice: ")
    return choice

def main():
    # Initialize the database schema
    createDB.create_schema()
    # Main loop
    while True:
        user_type = input("Are you a librarian or a client? (L/C): ").upper()
        
        if user_type == "L":
            while True:
                choice = librarian_menu()
                if choice == "1":
                    doc_choice = manage_documents_menu()
                    if doc_choice == "1":
                        insert_new_book()
                    elif doc_choice == "2":
                        update_document()
                    elif doc_choice == "3":
                        delete_document_copy()
                    elif doc_choice == "4":
                        break  # Go back to the main librarian menu
                elif choice == "2":
                    librarian_choice = manage_librarians_menu()
                    if librarian_choice == "1":
                        add_librarian()
                    elif librarian_choice == "2":
                        update_librarian()
                    elif librarian_choice == "3":
                        break  # Go back to the main librarian menu
                elif choice == "3":
                    client_management_menu()
                elif choice == "4":
                    view_lent_out_documents()
                elif choice == "5":
                    print("Exiting the program...")
                    return  # Exit the main program
                else:
                    print("Invalid choice. Please try again.")
        
        elif user_type == "C":
            while True:
                choice = client_menu()
                if choice == "1":
                    search_choice = search_documents_menu()
                    if search_choice == "1":
                        search_documents_by_title()
                    elif search_choice == "2":
                        print("Searching documents by author...")
                    elif search_choice == "3":
                        print("Searching documents by ISBN...")
                    elif search_choice == "4":
                        print("Searching documents by publisher...")
                    elif search_choice == "5":
                        print("Searching documents by edition...")
                    elif search_choice == "6":
                        print("Searching documents by year...")
                    elif search_choice == "7":
                        break  # Go back to the main client menu
                elif choice == "2":
                    borrow_document()
                elif choice == "3":
                    return_document()
                elif choice == "4":
                    print("Paying overdue fees...")
                elif choice == "5":
                    while True:
                        payment_choice = manage_payment_methods_menu()
                        if payment_choice == "1":
                            print("Adding payment method...")
                        elif payment_choice == "2":
                            print("Deleting payment method...")
                        elif payment_choice == "3":
                            break  # Go back to the main client menu
                elif choice == "6":
                    print("Exiting the program...")
                    return  # Exit the main program
                else:
                    print("Invalid choice. Please try again.")
        
        else:
            print("Invalid choice. Please enter 'L' for librarian or 'C' for client.")

if __name__ == "__main__":
    main()
main.py
20 KB