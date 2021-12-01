from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
ui = Tk()
ui.title("Password Manager")
<<<<<<< HEAD
ui.minsize(width=450, height=340)
=======
ui.minsize(width=450, height=250)
>>>>>>> 22f5a87bbb296f91bd9e47a04b76fb56fc62984e
ui.config(padx=20, pady=20)

logo_canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
logo_canvas.create_image(100, 100, image=logo)
logo_canvas.grid(row=0, column=1)
<<<<<<< HEAD
=======

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

website_input = Entry(width=35)
website_input.grid(row=1, column=1, columnspan=2, sticky="EW")

username_label = Label(text="Username/Email:")
username_label.grid(row=2, column=0)

username_input = Entry(width=35)
username_input.grid(row=2, column=1, columnspan=2, stick="EW")

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

password_input = Entry(width=21)
password_input.grid(row=3, column=1, sticky="WE")

generate_password_button = Button(text="Generate Password", width=14)
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")
>>>>>>> 22f5a87bbb296f91bd9e47a04b76fb56fc62984e

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

username_label = Label(text="Username/Email:")
username_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries
website_input = Entry(width=35)
website_input.grid(row=1, column=1, columnspan=2, sticky="EW")

username_input = Entry(width=35)
username_input.grid(row=2, column=1, columnspan=2, stick="EW")

password_input = Entry(width=21)
password_input.grid(row=3, column=1, sticky="EW")

# Buttons
generate_password_button = Button(text="Generate Password", width=14)
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")

# Mainloop
ui.mainloop()
