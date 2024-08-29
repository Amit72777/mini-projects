from tkinter import *
from tkinter import ttk, messagebox
import random
import pyperclip
import json


# _____________________________________ Search Password ___________________________#
def Search_password():
    website = website_var.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except:
        messagebox.showinfo(title="Error", message="NO DATA FILE FOUND")
    else:
        if website in data:
            messagebox.showinfo(title=website, message=f"website {website}\n"
                                                       f"email id :{data.get(website).get('email')}\n"
                                                            f" password = {data.get(website).get('password')}")
        else:
            messagebox.showinfo(title="Error", message=f"No details {website} exits.")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# generatoer a random password

def generatePassword():
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                'V', 'W', 'X', 'Y', 'Z',
                'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']

    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    special_characters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '{', '}', '[', ']', '|',
                          '\\', ';', ':', '"', "'", '<', '>', ',', '.', '?', '/']
    # taking input
    my_letter = random.randint(8, 11)

    my_symols = random.randint(2, 4)
    my_numbers = random.randint(2, 4)
    
    # add randome letter

    password_letter = [random.choice(alphabet) for _ in range(my_letter)]

    # add random symbols
    password_symbol = [random.choice(special_characters) for _ in range(my_symols)]

    # add random numbers
    password_number = [random.choice(numbers) for _ in range(my_numbers)]

    #  change place of list using shuffle function
    password_list = password_number + password_symbol + password_letter

    random.shuffle(password_list)
    # change list to string
    password = ''.join(password_list)
    password_entry.delete(0, END)
    pyperclip.copy(password)
    password_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_var.get()
    email = email_var.get()
    password = password_var.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }
    if not website or not email or not password:
        messagebox.showerror(title=website, message="Please don't leave any field empty")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Load the data
                data = json.load(data_file)

        except:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # update data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)

        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="#f7f5dd")

# Create a frame for better layout organization
frame = Frame(window, bg="#f7f5dd")
frame.grid(row=0, column=0, columnspan=3)

lock_img = PhotoImage(file="logo.png")
canvas = Canvas(frame, width=200, height=200, bg="#f7f5dd", highlightthickness=0)
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(frame, text="Website:", bg="#f7f5dd", fg="#333", font=("Arial", 12))
website_label.grid(row=1, column=0, pady=5)
email_label = Label(frame, text="Email/Username:", bg="#f7f5dd", fg="#333", font=("Arial", 12))
email_label.grid(row=2, column=0, pady=5)
password_label = Label(frame, text="Password:", bg="#f7f5dd", fg="#333", font=("Arial", 12))
password_label.grid(row=3, column=0, pady=5)

# Entries
website_var = StringVar()
website_entry = Entry(frame, width=30, textvariable=website_var, font=("Arial", 12))
website_entry.grid(row=1, column=1, padx=5)
website_entry.focus()

email_var = StringVar()
email_entry = Entry(frame, width=45, textvariable=email_var, font=("Arial", 12))
email_entry.grid(row=2, column=1, columnspan=2, padx=5)
email_entry.insert(0, "amitkushw2005@gmail.com")

password_var = StringVar()
password_entry = Entry(frame, width=30, textvariable=password_var, font=("Arial", 12))
password_entry.grid(row=3, column=1, padx=5)

# Buttons
generate_password_btn = ttk.Button(frame, text="Generate Password", command=generatePassword)
generate_password_btn.grid(row=3, column=2, padx=5)

add_btn = ttk.Button(frame, text="Add", width=70, command=save)
add_btn.grid(row=4, column=1, columnspan=2, pady=10)

search_btn = ttk.Button(frame, text="Search", width=20, command=Search_password)
search_btn.grid(row=1, column=2, padx=5)

window.mainloop()
