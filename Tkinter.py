import tkinter as tk

# Create the main window
root = tk.Tk()

# Set window title
root.title("My First Tkinter App")

# Set window size
root.geometry("400x200")

# Add a label
label = tk.Label(
    root,
    text="Hello from Tkinter!",
    font=("Arial", 16)
)

label.pack(pady=20)

# Add a button
def button_clicked():
    label.config(text="Button was clicked!")

button = tk.Button(
    root,
    text="Click Me",
    command=button_clicked
)

button.pack()

# Start the event loop
root.mainloop()