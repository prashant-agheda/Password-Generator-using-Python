# Importing the required Packages
from tkinter import *
from random import randint
import tkinter
import tkinter.messagebox

window = Tk()
window.title("Password Generator using Python - By Prashant Agheda")
window.geometry("600x400")


# Function to generate random password
def create_new_random_password():
    # 1st Clear the Entry box after user clicks on Generate password button
    password_entry.delete(0, END)

    # 2nd Get the password length
    # Wrapping the my_entry.get() into int to convert it into int because by default it returns str
    password_length = int(my_entry.get())

    # 3rd Create variable that holds our password
    my_pass = ""

    # 4th Loop through the password_length
    # If we type 15 in entry box then this will loop through 15 times
    for i in range(password_length):
        # This will generate a Random Integer between 34 to 125
        # Wrapping the randint(34, 125) so that it will convert that random int into ascii value
        # https://www.asciitable.com/
        my_pass += chr(randint(34, 125))

    # Display output on screen
    password_entry.insert(0, my_pass)


# Function to copy the password to clipboard
def copy_to_clipboard():
    # 1st Clear the clipboard
    window.clipboard_clear()

    # 2nd Copy to clipboard
    window.clipboard_append(password_entry.get())

    # 3rd Display message to user that password is copied to clipboard
    tkinter.messagebox.showinfo("From Password Generator", "Password Copied to Clipboard :)")



# Label that user will see
label_frame = LabelFrame(window, text="How many Characters you want?", font=("Arial", 18, "bold"))
label_frame.pack(pady=20)

# Input box for the user to enter the number of characters
my_entry = Entry(label_frame, font=("Arial", 26))
my_entry.pack(padx=20, pady=20)

# Input box to get our returned password so that we can copy the password
password_entry = Entry(window, text="", font=("Arial", 26), bd=0, bg="systembuttonface")
password_entry.pack(pady=20)

# Frame for Buttons
my_frame = Frame(window)
my_frame.pack(pady=20)

# Buttons
generate_password_button = Button(my_frame, text="Generate My Password", command=create_new_random_password, font=("Arial", 14), background="yellow")
generate_password_button.grid(row=0, column=0, padx=20)

copy_to_clipboard_button = Button(my_frame, text="Copy to Clipboard", command=copy_to_clipboard, font=("Arial", 14), background="yellow")
copy_to_clipboard_button.grid(row=0, column=1, padx=20)


window.mainloop()