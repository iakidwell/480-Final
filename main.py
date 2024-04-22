import createDB

def librarian_menu():
    print("Librarian Menu:")
    print("1. Manage Documents")
    print("2. Client Management")
    print("3. Exit")
    choice = input("Enter your choice: ")
    return choice

def manage_documents_menu():
    print("Manage Documents:")
    print("1. Insert New Document")
    print("2. Update Document")
    print("3. Delete Document Copy")
    print("4. Go Back to Librarian Menu")
    choice = input("Enter your choice: ")
    return choice

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
    # Call the function to create the database schema
    createDB.create_schema()
    # Main loop
    while True:
        user_type = input("Are you a librarian or a client? (L/C): ").upper()
        
        if user_type == "L":
            while True:
                choice = librarian_menu()
                if choice == "1":
                    while True:
                        doc_choice = manage_documents_menu()
                        if doc_choice == "1":
                            print("Inserting new document...")
                            # Implement insert document functionality
                        elif doc_choice == "2":
                            print("Updating document...")
                            # Implement update document functionality
                        elif doc_choice == "3":
                            print("Deleting document copy...")
                            # Implement delete document copy functionality
                        elif doc_choice == "4":
                            break
                        else:
                            print("Invalid choice. Please try again.")
                elif choice == "2":
                    while True:
                        client_choice = client_management_menu()
                        if client_choice == "1":
                            print("Registering new client...")
                            # Implement register new client functionality
                        elif client_choice == "2":
                            print("Updating client information...")
                            # Implement update client information functionality
                        elif client_choice == "3":
                            print("Deleting client...")
                            # Implement delete client functionality
                        elif client_choice == "4":
                            break
                        else:
                            print("Invalid choice. Please try again.")
                elif choice == "3":
                    print("Exiting the program...")
                    exit()
                else:
                    print("Invalid choice. Please try again.")

        elif user_type == "C":
            while True:
                choice = client_menu()
                if choice == "1":
                    while True:
                        search_choice = search_documents_menu()
                        if search_choice == "1":
                            print("Searching documents by title...")
                            # Implement search documents by title functionality
                        elif search_choice == "2":
                            print("Searching documents by author...")
                            # Implement search documents by author functionality
                        elif search_choice == "3":
                            print("Searching documents by ISBN...")
                            # Implement search documents by ISBN functionality
                        elif search_choice == "4":
                            print("Searching documents by publisher...")
                            # Implement search documents by publisher functionality
                        elif search_choice == "5":
                            print("Searching documents by edition...")
                            # Implement search documents by edition functionality
                        elif search_choice == "6":
                            print("Searching documents by year...")
                            # Implement search documents by year functionality
                        elif search_choice == "7":
                            break
                        else:
                            print("Invalid choice. Please try again.")
                elif choice == "2":
                    print("Borrowing a document...")
                    # Implement borrow document functionality
                elif choice == "3":
                    print("Returning a document...")
                    # Implement return document functionality
                elif choice == "4":
                    print("Paying overdue fees...")
                    # Implement pay overdue fees functionality
                elif choice == "5":
                    while True:
                        payment_choice = manage_payment_methods_menu()
                        if payment_choice == "1":
                            print("Adding payment method...")
                            # Implement add payment method functionality
                        elif payment_choice == "2":
                            print("Deleting payment method...")
                            # Implement delete payment method functionality
                        elif payment_choice == "3":
                            break
                        else:
                            print("Invalid choice. Please try again.")
                elif choice == "6":
                    print("Exiting the program...")
                    exit()
                else:
                    print("Invalid choice. Please try again.")

        else:
            print("Invalid choice. Please enter 'L' for librarian or 'C' for client.")

if __name__ == "__main__":
    main()