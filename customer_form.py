import tkinter as tk
from tkinter import ttk
import sqlite3

# Step 1: Create the main window
root = tk.Tk()
root.title("Customer Information")

# Step 2: Create labels and entry fields for each customer attribute
tk.Label(root, text="Name:").grid(row=0, column=0)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

tk.Label(root, text="Birthday (YYYY-MM-DD):").grid(row=1, column=0)
birthday_entry = tk.Entry(root)
birthday_entry.grid(row=1, column=1)

tk.Label(root, text="Email:").grid(row=2, column=0)
email_entry = tk.Entry(root)
email_entry.grid(row=2, column=1)

tk.Label(root, text="Phone Number:").grid(row=3, column=0)
phone_entry = tk.Entry(root)
phone_entry.grid(row=3, column=1)

tk.Label(root, text="Address:").grid(row=4, column=0)
address_entry = tk.Entry(root)
address_entry.grid(row=4, column=1)

tk.Label(root, text="Preferred Contact Method:").grid(row=5, column=0)
contact_method_combobox = ttk.Combobox(root, values=["Email", "Phone", "Mail"])
contact_method_combobox.grid(row=5, column=1)

# Step 3: Function to submit the form data to the database
def submit_customer_info():
    name = name_entry.get()
    birthday = birthday_entry.get()
    email = email_entry.get()
    phone_number = phone_entry.get()
    address = address_entry.get()
    preferred_contact_method = contact_method_combobox.get()

    # Step 4: Insert the customer data into the database
    conn = sqlite3.connect('customer_info.db')
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO customers (name, birthday, email, phone_number, address, preferred_contact_method)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', (name, birthday, email, phone_number, address, preferred_contact_method))
    conn.commit()
    conn.close()

    # Step 5: Clear the form after submission
    name_entry.delete(0, tk.END)
    birthday_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)
    contact_method_combobox.set("")

# Step 6: Create a Submit button
submit_button = tk.Button(root, text="Submit", command=submit_customer_info)
submit_button.grid(row=6, column=1)

# Step 7: Start the GUI event loop
root.mainloop()
