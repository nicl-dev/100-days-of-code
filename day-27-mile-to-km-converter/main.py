import tkinter

window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)

miles_input = tkinter.Entry(width=10)
miles_input.insert(0, "0")
miles_input.grid(row=0, column=1)

miles_label = tkinter.Label(text="Miles")
miles_label.grid(row=0, column=2)

is_equal_to = tkinter.Label(text="is equal to")
is_equal_to.grid(row=1, column=0)

kilometers_value = tkinter.Label(text="0")
kilometers_value.grid(row=1, column=1)

kilometers_label = tkinter.Label(text="Km")
kilometers_label.grid(row=1, column=2)


def calculate_kilometers():
    new_kilometers_value = float(miles_input.get()) * 1.609344
    kilometers_value.config(text=str(new_kilometers_value))


calculate_button = tkinter.Button(text="Calculate", command=calculate_kilometers)
calculate_button.grid(row=2, column=1)

window.mainloop()
