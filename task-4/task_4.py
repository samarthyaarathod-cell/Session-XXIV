import tkinter as tk

# Create the main window
root = tk.Tk()

# Set window title
root.title("Login Form")

# Set window size
root.geometry("400x300")


# Function to check login
def login():
    username = username_entry.get()
    password = password_entry.get()

    if username != "" and password != "":
        message_label.config(text="Login Successful")
    else:
        message_label.config(text="Please enter Username and Password")


# Heading
heading_label = tk.Label(
    root,
    text="Login Form",
    font=("Arial", 20, "bold")
)
heading_label.grid(row=0, column=0, columnspan=2, pady=20)


# Username label
username_label = tk.Label(
    root,
    text="Username:"
)
username_label.grid(row=1, column=0, padx=10, pady=10)


# Username entry
username_entry = tk.Entry(root, width=25)
username_entry.grid(row=1, column=1, padx=10, pady=10)


# Password label
password_label = tk.Label(
    root,
    text="Password:"
)
password_label.grid(row=2, column=0, padx=10, pady=10)


# Password entry
password_entry = tk.Entry(
    root,
    width=25,
    show="*"
)
password_entry.grid(row=2, column=1, padx=10, pady=10)


# Login button
login_button = tk.Button(
    root,
    text="Login",
    width=12,
    command=login
)
login_button.grid(row=3, column=0, columnspan=2, pady=15)


# Message label
message_label = tk.Label(
    root,
    text="",
    font=("Arial", 12)
)
message_label.grid(row=4, column=0, columnspan=2, pady=10)


# Run the application
root.mainloop()