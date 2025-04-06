import sqlite3
import tkinter as tk
from tkinter import messagebox
import re

# Function to validate email format
def validate_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

# Function to validate phone number format (must be 10 digits)
def validate_phone(phone):
    return phone.isdigit() and len(phone) == 10

# Function to handle form submission
def submit_form():
    # Retrieve the input values from the form
    name = name_entry.get()
    birthday = birthday_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    address = address_entry.get()
    contact_method = contact_method_var.get()

    # Validation for required fields
    if not (name and birthday and email and phone and address and contact_method):
        messagebox.showerror("Error", "All fields are required!")
        return
    
    # Validate email format
    if not validate_email(email):
        messagebox.showerror("Error", "Invalid email format!")
        return
    
    # Validate phone number format
    if not validate_phone(phone):
        messagebox.showerror("Error", "Phone number must be 10 digits!")
        return

    # Save data into the SQLite database
    try:
        conn = sqlite3.connect('customer_info.db')  # Connect to the database (or create it if it doesn't exist)
        cursor = conn.cursor()

        # Insert the data into the 'customers' table
        cursor.execute('''
            INSERT INTO customers (name, birthday, email, phone, address, preferred_contact_method)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (name, birthday, email, phone, address, contact_method))

        # Commit the transaction
        conn.commit()
        conn.close()

        # Clear the form after successful submission
        name_entry.delete(0, tk.END)
        birthday_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
        address_entry.delete(0, tk.END)
        contact_method_var.set('')  # Reset dropdown to default value

        # Show success message
        messagebox.showinfo("Success", "Customer information submitted successfully!")
    
    except sqlite3.Error as e:
        messagebox.showerror("Database Error", f"Error saving data: {e}")

# Create the main Tkinter window
root = tk.Tk()
root.title("Customer Information Form")

# Name field
name_label = tk.Label(root, text="Name:")
name_label.grid(row=0, column=0)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

# Birthday field
birthday_label = tk.Label(root, text="Birthday (YYYY-MM-DD):")
birthday_label.grid(row=1, column=0)
birthday_entry = tk.Entry(root)
birthday_entry.grid(row=1, column=1)

# Email field
email_label = tk.Label(root, text="Email:")
email_label.grid(row=2, column=0)
email_entry = tk.Entry(root)
email_entry.grid(row=2, column=1)

# Phone field
phone_label = tk.Label(root, text="Phone Number:")
phone_label.grid(row=3, column=0)
phone_entry = tk.Entry(root)
phone_entry.grid(row=3, column=1)

# Address field
address_label = tk.Label(root, text="Address:")
address_label.grid(row=4, column=0)
address_entry = tk.Entry(root)
address_entry.grid(row=4, column=1)

# Preferred contact method dropdown
contact_method_label = tk.Label(root, text="Preferred Contact Method:")
contact_method_label.grid(row=5, column=0)

contact_method_var = tk.StringVar()
contact_method_var.set('Email')  # Default to "Email"
contact_method_menu = tk.OptionMenu(root, contact_method_var, 'Email', 'Phone')
contact_method_menu.grid(row=5, column=1)

# Submit button
submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button.grid(row=6, column=0, columnspan=2)

# Start the Tkinter event loop
root.mainloop()
