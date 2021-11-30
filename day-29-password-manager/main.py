from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
ui = Tk()
ui.title("Password Manager")
ui.minsize(width=250, height=250)
ui.config(padx=20, pady=20)

logo_canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
logo_canvas.create_image(100, 100, image=logo, anchor=CENTER)
logo_canvas.grid(row=0, column=0)

ui.mainloop()
