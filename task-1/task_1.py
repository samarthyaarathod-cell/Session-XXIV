# Task:-
# 1. Create a Tkinter window titled 'My Playlist' that displays a label saying 'Welcome to Your Music Playlist' at the top center of the window.

import tkinter as tk

# Create the main window
root = tk.Tk()

# Set window title
root.title("My Playlist")

# Set window size
root.geometry("500x300")

# Create welcome label
welcome_label = tk.Label(
    root,
    text="Welcome to Your Music Playlist",
    font=("Arial", 18, "bold")
)

# Place label at the top center
welcome_label.pack(pady=30)

# Run the application
root.mainloop()