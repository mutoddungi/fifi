import tkinter as tk

def increase_yes_size():
    global yes_width, yes_height
    yes_width += 5
    yes_height += 2
    yes_button.config(width=yes_width, height=yes_height)

def no_clicked():
    no_button.config(text="Are you sure?")
    increase_yes_size()

# Initialize Tkinter window
root = tk.Tk()
root.title("Valentine Proposal Game")
root.configure(bg='pink')  # Set background color to pink

# Initial button size
yes_width = 10
yes_height = 2

# Label
label = tk.Label(root, text="Will you be my Valentine?", font=("Arial", 14), bg='pink')
label.pack(pady=10)

# YES Button
yes_button = tk.Button(root, text="YES", width=yes_width, height=yes_height, bg='green', fg='white', command=lambda: label.config(text="Yay! ❤️"))
yes_button.pack(pady=10)

# NO Button
no_button = tk.Button(root, text="NO", width=10, height=2, bg='red', fg='white', command=no_clicked)
no_button.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()