# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import random
import pyperclip
import json
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    p_letter = [random.choice(letters) for i in range(nr_letters)]
    p_symbol = [random.choice(symbols) for i in range(nr_symbols)]
    p_number = [random.choice(numbers) for i in range(nr_numbers)]

    password_list = p_letter + p_number + p_symbol

    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(END, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
from tkinter import messagebox
def save():
    website = website_entry.get().title()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website:{
            "email":email,
            "password":password
        }
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure no field(s) are empty")  
    else:
        try:
            with open("./data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("./data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)

            with open("./data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

#------------------Find Password--------------------------------#
def find_password():
    website = website_entry.get().title()
    try:
        with open("./data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found!")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exist")
# ---------------------------- UI SETUP ------------------------------- #
from tkinter import *
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)


canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="./logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label()
website_label.config(text="Website:")
website_label.grid(column=0, row=1)

website_entry = Entry()
website_entry.config(width=25)
website_entry.focus()
website_entry.grid(column=1, row=1,)

label_email = Label()
label_email.config(text="Email/Username:")
label_email.grid(column=0, row=2)

email_entry = Entry()
email_entry.config(width=35)
email_entry.insert(0, "adekomuheez567@gmail.com")
email_entry.grid(column=1, row=2, columnspan=2)

label_password = Label()
label_password.config(text="Password:")
label_password.grid(column=0, row=3)

password_entry = Entry()
password_entry.config(width=21)
password_entry.grid(column=1, row=3)

gen_password = Button()
gen_password.config(text="Generate Password", highlightthickness=0, command=generate_password)
gen_password.grid(column=2, row=3)

add_btn = Button()
add_btn.config(text="Add", highlightthickness=0, width=36, command=save)
add_btn.grid(column=1, row=4, columnspan=2)

search_btn = Button()
search_btn.config(text="Search", highlightthickness=0,width=18, command=find_password)
search_btn.grid(column=2, row=1)























window.mainloop()
