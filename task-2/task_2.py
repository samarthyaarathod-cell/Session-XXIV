import tkinter as tk

# Create the main window
root = tk.Tk()

# Set window title
root.title("My Playlist")

# Set window size
root.geometry("500x350")


# Function to update the status label
def update_status(message):
    status_label.config(text=message)


# Welcome label
welcome_label = tk.Label(
    root,
    text="Welcome to Your Music Playlist",
    font=("Arial", 18, "bold")
)
welcome_label.pack(pady=30)


# Create a frame for the buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=20)


# Play button
play_button = tk.Button(
    button_frame,
    text="Play",
    width=10,
    command=lambda: update_status("Playing")
)
play_button.grid(row=0, column=0, padx=10)


# Pause button
pause_button = tk.Button(
    button_frame,
    text="Pause",
    width=10,
    command=lambda: update_status("Paused")
)
pause_button.grid(row=0, column=1, padx=10)


# Next button
next_button = tk.Button(
    button_frame,
    text="Next",
    width=10,
    command=lambda: update_status("Next Song")
)
next_button.grid(row=0, column=2, padx=10)


# Status label
status_label = tk.Label(
    root,
    text="Select an action",
    font=("Arial", 14)
)
status_label.pack(pady=20)


# Run the application
root.mainloop()