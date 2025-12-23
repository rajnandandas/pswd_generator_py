import string
import secrets
import pyperclip
import tkinter as tk
from tkinter import messagebox
# Make sure pyperclip is installed


def generate_password():
    """
    Function for generating password as name suggests. First it creates a character set
    and populates it with uppercase alphabet, lowercase alphabet, numerical digits and
    special characters, depending on which of these four categories are enabled. Then using
    secrets module we randomly select character from the character set, n times, where n is
    the acceptable valid integer that denotes the password length required.
    """
    
    try: 
        length = int(length_entry.get())
    except ValueError as e:
        messagebox.showerror("Error","Please enter a number.")
        return
    use_upper = upper_var.get()
    use_lower = lower_var.get()
    use_digits = digit_var.get()
    use_special = special_var.get()

    characters = ''
    if use_upper:characters += string.ascii_uppercase
    if use_lower:characters += string.ascii_lowercase
    if use_digits:characters += string.digits
    if use_special:characters += string.punctuation

    if not characters:
        messagebox.showerror("Error", "Please select at least one character type.")
        return
    if length<=0:
        messagebox.showerror("Error","Password length should be greater than 0. Please check again.")
        return

    password = ''.join(secrets.choice(characters) for _ in range(length))
    password_var.set(password)
    return

def copy_to_clipboard():
    """
    This function is to generate a message if a password has been copied.
    """
    password = password_var.get()
    if password:
        pyperclip.copy(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    return

# GUI Setup
root = tk.Tk()
root.title("RPG - Random Password Generator")
root.geometry("400x350")
root.resizable(False, False)

# Widgets
tk.Label(root, text="Password Length:",font=('Arial',12)).pack(pady=5)
length_entry_min = tk.Entry(root)
length_entry_min.insert(0, "12")
length_entry_min.pack()
length_entry_max = tk.Entry(root)
length_entry_max.insert(0, "12")
length_entry_max.pack()
tk.Label(root, text="recommended length: 8-12").pack(pady=2)

# tk.Label(root, text="Min:",font=('Arial',12)).pack(padx=5)
# length_entry_min = tk.Entry(root)
# length_entry_min.insert(0, "8")
# length_entry_min.pack(padx=5)
# tk.Label(root, text="Max:",font=('Arial',12)).pack(padx=10)
# length_entry_max = tk.Entry(root)
# length_entry_max.insert(0, "12")
# length_entry_max.pack(padx=5)

upper_var = tk.BooleanVar(value=True)
lower_var = tk.BooleanVar(value=True)
digit_var = tk.BooleanVar(value=True)
special_var = tk.BooleanVar(value=True)

tk.Checkbutton(root, text="Include Uppercase", variable=upper_var,font=('Arial',12)).pack()
tk.Checkbutton(root, text="Include Lowercase", variable=lower_var,font=('Arial',12)).pack()
tk.Checkbutton(root, text="Include Digits", variable=digit_var,font=('Arial',12)).pack()
tk.Checkbutton(root, text="Include Special Characters", variable=special_var,font=('Arial',12)).pack()

tk.Button(root, text="Generate Password", command=generate_password,font=('Arial',12)).pack(pady=10)

password_var = tk.StringVar()
tk.Entry(root, textvariable=password_var, font=("Helvetica", 12), justify="center", state="readonly").pack(pady=5)

tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard,font=('Arial',12)).pack(pady=5)

root.mainloop()