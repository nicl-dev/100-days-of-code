import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label
my_label = tkinter.Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.pack()
my_label["text"] = "New Text"

# Entry
user_input = tkinter.Entry(width=10)
user_input.pack()


# Button
def button_clicked():
    new_text = user_input.get()
    my_label.config(text=new_text)


button = tkinter.Button(text="Click me", command=button_clicked)
button.pack()

window.mainloop()
