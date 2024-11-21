import tkinter as tk
import random
import string

# Function to generate a random password
def gen_pass(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    password_entry.delete(0, tk.END)  # Clear the current entry
    password_entry.insert(0, password)  # Insert the new password

# Function to update the password length label
def update_length_label(value):
    length_label.config(text=f"Password Length: {value}")

# Create the main window
root = tk.Tk()
root.title("Random Password Generator")

# Create a slider for password length
slider = tk.Scale(root, from_=25, to=255, orient=tk.HORIZONTAL, command=update_length_label)
slider.set(25)  # Set the default length to 25
slider.pack(pady=20)

# Create a label to display the current length
length_label = tk.Label(root, text="Password Length: 25")
length_label.pack()

# Create an entry to display the generated password
password_entry = tk.Entry(root, width=50, font=("Arial", 14))
password_entry.pack(pady=20)

# Create a button to generate the password
generate_button = tk.Button(root, text="Generate Password", command=lambda: gen_pass(slider.get()))
generate_button.pack(pady=20)

# Run the application
root.mainloop()