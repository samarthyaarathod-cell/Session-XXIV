import tkinter as tk

# Create the main window
root = tk.Tk()

# Set window title
root.title("Music Options")

# Set window size
root.geometry("400x300")


# Create a frame to hold the buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=50)


# Like button
like_button = tk.Button(
    button_frame,
    text="Like",
    width=15,
    height=2
)
like_button.grid(row=0, column=0, padx=10, pady=10)


# Share button
share_button = tk.Button(
    button_frame,
    text="Share",
    width=15,
    height=2
)
share_button.grid(row=0, column=1, padx=10, pady=10)


# Download button
download_button = tk.Button(
    button_frame,
    text="Download",
    width=15,
    height=2
)
download_button.grid(row=1, column=0, padx=10, pady=10)


# Add to Queue button
queue_button = tk.Button(
    button_frame,
    text="Add to Queue",
    width=15,
    height=2
)
queue_button.grid(row=1, column=1, padx=10, pady=10)


# Run the application
root.mainloop()