import sqlite3

# Create a connection to the SQLite database (or create one if it doesn't exist)
conn = sqlite3.connect('customer_info.db')

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Create the table to store customer information
cursor.execute('''
CREATE TABLE IF NOT EXISTS customers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    birthday TEXT NOT NULL,
    email TEXT NOT NULL,
    phone_number TEXT NOT NULL,
    address TEXT NOT NULL,
    preferred_contact_method TEXT NOT NULL
)
''')

# Commit the changes and close the connection
conn.commit()
conn.close()
