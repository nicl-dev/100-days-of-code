import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label
my_label = tkinter.Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.grid(row=0, column=0)
my_label["text"] = "New Text"

# Entry
user_input = tkinter.Entry(width=15)
user_input.insert(0, "Enter something.")
user_input.grid(row=2, column=3)


# Button
def button_clicked():
    new_text = user_input.get()
    my_label.config(text=new_text)


button = tkinter.Button(text="Click me", command=button_clicked)
button.grid(row=1, column=1)

new_button = tkinter.Button(text="I am a new button.")
new_button.grid(row=0, column=2)

window.mainloop()
