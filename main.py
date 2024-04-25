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

def manage_documents_menu():
    print("Manage Documents:")
    print("1. Insert New Document")
    print("2. Update Document")
    print("3. Delete Document Copy")
    print("4. View Document")
    print("5. Go Back to Librarian Menu")
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

def view_document_details():
    choice = input("Do you want to view all documents or a specific document? (all/specific): ").lower()
    with sqlite3.connect('library.db') as conn:
        cursor = conn.cursor()
        if choice == "specific":
            isbn = input("Enter the ISBN of the document: ")
            cursor.execute("SELECT * FROM book WHERE isbn = ?", (isbn,))
            book = cursor.fetchone()
            if book:
                print(f"ISBN: {book[0]}, Title: {book[1]}, Publisher: {book[2]}, Edition: {book[3]}, Number of Pages: {book[4]}")
                cursor.execute("SELECT author FROM book_authors WHERE isbn = ?", (isbn,))
                authors = cursor.fetchall()
                print("Authors: " + ", ".join(author[0] for author in authors))
            else:
                print("No document found with the given ISBN.")
        elif choice == "all":
            cursor.execute("SELECT * FROM book")
            books = cursor.fetchall()
            if books:
                print("All documents in the library:")
                for book in books:
                    print(f"ISBN: {book[0]}, Title: {book[1]}, Publisher: {book[2]}, Edition: {book[3]}, Number of Pages: {book[4]}")
                    cursor.execute("SELECT author FROM book_authors WHERE isbn = ?", (book[0],))
                    authors = cursor.fetchall()
                    print("Authors: " + ", ".join(author[0] for author in authors))
                    print("-" * 40)
            else:
                print("No documents found in the library.")
        else:
            print("Invalid choice. Please enter 'all' or 'specific'.")

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
                cursor.execute("INSERT INTO client_addresses (client_email, address) VALUES (?, ?)", (email, address))
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

# Search functions
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

def search_documents_by_author():
    author_search = input("Enter the author of books: ")

    with sqlite3.connect('library.db') as conn:
            cursor = conn.cursor()
            cursor.execute("""
                        SELECT b.isbn, b.title, b.publisher 
                        FROM book b 
                        JOIN book_authors ba ON b.isbn = ba.isbn 
                        WHERE ba.author LIKE ?
                    """, ('%' + author_search + '%',))
            books = cursor.fetchall()
            
            if books:
                print("Books found:")
                for book in books:
                    print(f"ISBN: {book[0]}, Title: {book[1]}, Publisher: {book[2]}")
            else:
                print("No books found with the given author.")

def search_documents_by_isbn():
    isbn_search = input("Enter ISBN of book: ")

    with sqlite3.connect('library.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT isbn, title, publisher, edition, num_pages FROM book WHERE isbn = ?", (isbn_search,))
        books = cursor.fetchall()

        if books:
            print("Books found: ")
            for book in books:
                print(f"ISBN: {book[0]}, Title: {book[1]}, Publisher: {book[2]}")
        else:
            print("No books found with the given ISBN. ")

def search_documents_by_publisher():
    publisher_search = input("Enter publisher of book: ")

    with sqlite3.connect('library.db') as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT isbn, title, publisher 
            FROM book 
            WHERE publisher LIKE ?
        """, ('%' + publisher_search + '%',))

        books = cursor.fetchall()

        if books:
            print("Books found:")
            for book in books:
                print(f"ISBN: {book[0]}, Title: {book[1]}, Publisher: {book[2]}")
        else:
            print("No books found with the given publisher")

def search_documents_by_edition():
    edition_search = input("Enter edition of book")

    with sqlite3.connect('library.db') as conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT isbn, title, publisher, edition
                       FROM book
                       WHERE edition LIKE ?
                        """, ('%' + edition_search + '%',))        
        books = cursor.fetchall()

        if books:
            print("Books found:")
            for book in books:
                print(f"ISBN: {book[0]}, Title: {book[1]}, Publisher: {book[2]}, Edition: {book[3]}")
        else:
            print("No books found with the given publisher")

def search_document_by_year():
    year_search = input("Enter year of book: ")

    with sqlite3.connect('library.db') as conn:
        cursor = conn.cursor()
        cursor.execute("""
                       SELECT isbn, title, publisher, year
                       FROM book
                       WHERE year LIKE ?
                       """, ('%' + year_search + '%',))
        books = cursor.fetchall()

        if books:
            print("Books found:")
            for book in books:
                print(f"ISBN: {book[0]}, Title: {book[1]}, Publisher: {book[2]}, Edition: {book[3]}")

        else: 
            print("No books found with the given year")

# Payment Method functions
def add_payment_methods():
    with sqlite3.connect('library.db') as conn:
        cursor = conn.cursor()

        #User input
        email = input("Enter the client email: ")
        credit_card_number = input("Enter the credit card number: ")
        address_id = input("Enter address of client: ")

        #Validate email
        cursor.execute("SELECT email FROM client WHERE email = ?", (email,))
        if not cursor.fetchone():
            print("No client found with given email.")
            return#Exit
        
        #Validate address
        #cursor.execute("SELECT address_id FROM client_addresses WHERE email = ? AND address_id = ?", (email, address_id))
        #if not cursor.fetchone():
        #    print("Invalid address for the given client.")
        #    return
        
        #Attempt to entry credit card information
        try:
            cursor.execute("""
                            INSERT INTO credit_cards (client_email, credit_card_number, address_id) 
                            VALUES (?, ?, ?) """,
                           (email, credit_card_number, address_id))
            conn.commit()
            print("Payment method added succesfully.")
        except sqlite3.IntegrityError as e:
            print(f"Failed to add payment method. Error: {e}")

def delete_payment_methods():

    with sqlite3.connect('library.db') as conn:
        cursor = conn.cursor()

        #Input user
        email = input("Enter Clients email: ")
        credit_card_number = input("Enter the credit card number: ")

        #Validate the clients email
        cursor.execute("SELECT email FROM client WHERE email = ?", (email,))
        if not cursor.fetchone():
            print("Invalid email address with given uesr")
            return#exit
        
        #Validate Credit card number
        cursor.execute("SELECT credit_card_number FROM credit_cards WHERE client_email = ? AND credit_card_number = ?", (email, credit_card_number))
        if not cursor.fetchone():
            print("No credit card number exists")
            return#exit
        
        #Attempt to remove credit card
        try:
            cursor.execute("DELETE FROM credit_cards WHERE client_email = ? AND credit_card_number = ?", (email, credit_card_number))
            conn.commit()
            print("Credit card delete successfully.")
        except sqlite3.Error as e:
            print(f"Failed to delete the credit card. Error: {e}")
                                                   
def display_payment_options():

    with sqlite3.connect('library.db') as conn:
        cursor = conn.cursor()

        #Input user
        email = input("Enter clients email: ")


        #Validate email
        cursor.execute("SELECT email FROM client WHERE email = ?", (email,))
        if not cursor.fetchone():
            print("Invalid email addresss with given user")
            return#exit


        # Fetch and display credit card details
        cursor.execute("""
            SELECT credit_card_number, address_id 
            FROM credit_cards 
            WHERE client_email = ?
        """, (email,))

        cards = cursor.fetchall()
        if cards:
            for card in cards:
                print(f"Credit Card Number: {card[0]}, Address ID: {card[1]}")
        else:
            print("No payment methods found for this client.")
        
#Updated
def manage_payment_debt():
    with sqlite3.connect('library.db') as conn:
        cursor = conn.cursor()

        #User input
        email = input("Enter clients email")
        credit_card_number = input("Enter payment card")

        #Validate user email
        cursor.execute("SELECT email FROM client WHERE email = ?", (email,))
        if not cursor.fetchone():
            print("Invalid email address with given user")
            return#exit
        
        #Validate payment card
        cursor.execute("SELECT credit_card_number FROM credit_cards WHERE client_email = ? AND credit_card_number = ?", (email, credit_card_number))
        if not cursor.fetchone():
            print("Invalid payment method.")
            return#exit
        
        #Check overdue fee's
        cursor.execute("SELECT overdue_fees FROM client WHERE email = ?", (email,))
        overdue_fees = cursor.fetchone()

        #Attempt to make payments
        if overdue_fees and overdue_fees[0] > 0:
            print(f"Payment processing for overdue fees ${overdue_fees[0]:.2f}.")
            cursor.execute("UPDATE client SET overdue_fees = 0 WHERE email = ?", (email,))
            conn.commit()
            print("Payment successful. Overdue fees cleared")
        elif overdue_fees and overdue_fees[0] == 0:
            print("User has no overdue fees")
        else:
            print("Failed to pull overdue fees.")

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
    try:
        with sqlite3.connect('library.db') as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT cl.email, b.title, cl.due_date
                FROM client_loans cl
                JOIN book b ON cl.isbn = b.isbn
                WHERE cl.returned = 0
            """)
            loans = cursor.fetchall()
            if loans:
                print("Currently Lent Out Documents:")
                for loan in loans:
                    print(f"Client Email: {loan[0]}, Title: {loan[1]}, Due Date: {loan[2]}")
            else:
                print("No documents are currently lent out.")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

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

#Added if branches
#Removed return
#Updated
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

    if choice == "1":
        search_documents_by_title()
    elif choice == "2":
        search_documents_by_author()
    elif choice == "3":
        search_documents_by_isbn()
    elif choice == "4":
        search_documents_by_publisher()
    elif choice == "5":
        search_documents_by_edition()
    elif choice == "6":
        search_document_by_year()
    elif choice == "7":
        return  # exit

def manage_payment_methods_menu():
    print("Manage Payment Methods:")
    print("1. Add Payment Method")
    print("2. Delete Payment Method")
    print("3. View Payment Methods")
    print("4. Go Back to Client Menu")
    choice = input("Enter your choice: ")
    return choice

def manage_payment_debt():
    with sqlite3.connect('library.db') as conn:
        cursor = conn.cursor()

        #User input
        email = input("Enter clients email")
        credit_card_number = input("Enter payment card")

        #Validate user email
        cursor.execute("SELECT email FROM client WHERE email = ?", (email,))
        if not cursor.fetchone():
            print("Invalid email address with given user")
            return#exit
        
        #Validate payment card
        cursor.execute("SELECT credit_card_number FROM credit_cards WHERE client_email = ? AND credit_card_number = ?", (email, credit_card_number))
        if not cursor.fetchone():
            print("Invalid payment method.")
            return#exit
        
        #Check overdue fee's
        cursor.execute("SELECT overdue_fees FROM client WHERE email = ?", (email,))
        overdue_fees = cursor.fetchone()

        #Attempt to make payments
        if overdue_fees and overdue_fees[0] > 0:
            print(f"Payment processing for overdue fees ${overdue_fees[0]:.2f}.")
            cursor.execute("UPDATE client SET overdue_fees = 0 WHERE email = ?", (email,))
            conn.commit()
            print("Payment successful. Overdue fees cleared")
        elif overdue_fees and overdue_fees[0] == 0:
            print("User has no overdue fees")
        else:
            print("Failed to pull overdue fees.")

def authenticate_user(email, password):
    with sqlite3.connect('library.db') as conn:
        cursor = conn.cursor()

        # Check if the email and password match a librarian record
        cursor.execute("SELECT email FROM librarian WHERE email = ? AND password = ?", (email, password))
        librarian = cursor.fetchone()
        if librarian:
            return "LIBRARIAN"

        # Check if the email and password match a client record
        cursor.execute("SELECT email FROM client WHERE email = ? AND password = ?", (email, password))
        client = cursor.fetchone()
        if client:
            return "CLIENT"

        # No match found
        return None

def main():
    # Initialize the database schema
    createDB.create_schema()
    
    while True:
        # Prompt for login
        email = input("Enter your email: ")
        password = input("Enter your password: ")

        # Check if login credentials match librarian or client records
        user_role = authenticate_user(email, password)
        if user_role == "LIBRARIAN":
            while True:
                choice = librarian_menu()
                if choice == "1":
                    while True:
                        doc_choice = manage_documents_menu()
                        if doc_choice == "1":
                            insert_new_book()
                        elif doc_choice == "2":
                            update_document()
                        elif doc_choice == "3":
                            delete_document_copy()
                        elif doc_choice == "4":
                            view_document_details()  # Call the function to view document details
                        elif doc_choice == "5":
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
                    client_management_choice = client_management_menu()
                    if client_management_choice == "1":
                        register_new_client()
                    elif client_management_choice == "2":
                        update_client_information()
                    elif client_management_choice == "3":
                        delete_client()
                    elif client_management_choice == "4":
                        break  # Go back to the main librarian menu
                elif choice == "4":
                    view_lent_out_documents()
                elif choice == "5":
                    print("Exiting the program...")
                    return  # Exit the main program
                else:
                    print("Invalid choice. Please try again.")
        elif user_role == "CLIENT":
            while True:
                choice = client_menu()
                if choice == "1":
                    search_choice = search_documents_menu()
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
                            add_payment_methods()
                        elif payment_choice == "2":
                            delete_payment_methods()
                        elif payment_choice == "3":
                            display_payment_options()
                        elif payment_choice == "4":
                            break  # Go back to the main client menu
                elif choice == "6":
                    print("Exiting the program...")
                    return  # Exit the main program
                else:
                    print("Invalid choice. Please try again.")
        else:
            print("Invalid email or password. Please try again.")

if __name__ == "__main__":
    main()
