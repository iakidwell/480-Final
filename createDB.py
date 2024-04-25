import sqlite3

# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect('library.db')
cursor = conn.cursor()

# Create tables
def create_schema():
    #cursor.execute('''
    #    CREATE TABLE IF NOT EXISTS log (
    #        email VARCHAR(255) PRIMARY KEY,
    #        password VARCHAR(255)
    #    )
    #''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS credit_cards (
            client_email VARCHAR(255),
            credit_card_number VARCHAR(16),
            address_id INTEGER,
            PRIMARY KEY (client_email, credit_card_number),
            FOREIGN KEY (client_email) REFERENCES client(email),
            FOREIGN KEY (address_id) REFERENCES client_addresses(address_id)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS client (
            email VARCHAR(255) PRIMARY KEY,
            overdue_fees DECIMAL(10, 2),
            name VARCHAR(255),
            password VARCHAR(255)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS client_addresses (
            email VARCHAR(255),
            address VARCHAR(255),
            PRIMARY KEY (email, address),
            FOREIGN KEY (email) REFERENCES client(email)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS client_credit_cards (
            email VARCHAR(255),
            credit_card_number VARCHAR(16),
            PRIMARY KEY (email, credit_card_number),
            FOREIGN KEY (email) REFERENCES client(email)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS client_loans (
            email TEXT NOT NULL,
            copy_number INTEGER NOT NULL,
            due_date TEXT NOT NULL,
            returned INTEGER DEFAULT 0,
            PRIMARY KEY (email, copy_number),
            FOREIGN KEY (email) REFERENCES client(email),
            FOREIGN KEY (copy_number) REFERENCES document(copy_number)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS librarian (
            SSN VARCHAR(255) PRIMARY KEY,
            name VARCHAR(255),
            email VARCHAR(255),
            password VARCHAR(255),
            salary DECIMAL(10, 2)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS librarian_client (
            librarian_SSN VARCHAR(255),
            client_email VARCHAR(255),
            PRIMARY KEY (librarian_SSN, client_email),
            FOREIGN KEY (librarian_SSN) REFERENCES librarian(SSN),
            FOREIGN KEY (client_email) REFERENCES client(email)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS document (
            copy_number INT PRIMARY KEY,
            isbn TEXT NOT NULL,
            on_loan BOOLEAN NOT NULL DEFAULT 0,
            FOREIGN KEY (isbn) REFERENCES book(isbn)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS journal_article (
            title VARCHAR(255) PRIMARY KEY,
            journal_name VARCHAR(255),
            isbn VARCHAR(13),
            issue_number INT,
            publisher VARCHAR(255),
            copy_number INT,
            on_loan BOOLEAN,
            year INT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS journal_article_authors (
            title VARCHAR(255),
            author VARCHAR(255),
            PRIMARY KEY (title, author),
            FOREIGN KEY (title) REFERENCES journal_article(title)
        )
    ''')

#    cursor.execute('''
#        CREATE TABLE IF NOT EXISTS bound_document (
#            isbn VARCHAR(13) PRIMARY KEY,
#            publisher VARCHAR(255)
#        )
#    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS magazine (
            isbn VARCHAR(13) PRIMARY KEY,
            publisher VARCHAR(255),
            magazine_name VARCHAR(255),
            month VARCHAR(255)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS book (
            isbn VARCHAR(13) PRIMARY KEY,
            publisher VARCHAR(255),
            title VARCHAR(255),
            edition VARCHAR(255),
            num_pages INT,
            copy_number INT,
            on_loan BOOLEAN,
            year INT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS book_authors (
            isbn TEXT NOT NULL,
            author TEXT NOT NULL,
            PRIMARY KEY (isbn, author),
            FOREIGN KEY (isbn) REFERENCES book(isbn)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS client_documents (
            email VARCHAR(255),
            copy_number INT,
            PRIMARY KEY (email, copy_number),
            FOREIGN KEY (email) REFERENCES client(email),
            FOREIGN KEY (copy_number) REFERENCES document(copy_number)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS librarian_documents (
            SSN VARCHAR(255),
            copy_number INT,
            PRIMARY KEY (SSN, copy_number),
            FOREIGN KEY (SSN) REFERENCES librarian(SSN),
            FOREIGN KEY (copy_number) REFERENCES document(copy_number)
        )
    ''')

    # Insert default admin librarian
    cursor.execute("INSERT OR IGNORE INTO librarian (SSN, name, email, password, salary) VALUES (?, ?, ?, ?, ?)",
                   ("111-11-1111", "Admin Librarian", "admin-librarian@example.com", "admin123", 0.00))

    # Insert default admin client
    cursor.execute("INSERT OR IGNORE INTO client (email, password, overdue_fees, name) VALUES (?, ?, ?, ?)",
                   ("admin-client@example.com", "admin123", 0.00, "Admin Client"))

    # Ensuring indexes are created for efficient searching
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_book_title ON book(title)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_book_isbn ON book(isbn)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_authors_name ON book_authors(author)")
    cursor.execute("ALTER TABLE client_loans ADD COLUMN due_date TEXT NOT NULL")

    # Commit changes and close connection
    conn.commit()
    conn.close()

    print("Database schema created successfully.")