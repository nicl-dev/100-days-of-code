from tkinter import  *

# CONSTANTS

BACKGROUND_COLOR = "#aed9c2"

root = Tk()
root.title("Flash Cards")
root.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
root.minsize(width=900, height=626)

# Setup Images
card_back = PhotoImage(file="images/card_back.png")
card_front = PhotoImage(file="images/card_front.png")
right = PhotoImage(file="images/right.png")
wrong = PhotoImage(file="images/wrong.png")

# Canvas
card_canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_canvas.create_image(400, 263, image=card_front)
card_canvas.create_text(400, 150, text="French", font=("Arial", 40, "italic"))
card_canvas.create_text(400, 263, text="trouve", font=("Arial", 60, "bold"))
card_canvas.grid(row=0, column=0, columnspan=2)

# Buttons
right_button = Button(image=right, highlightthickness=0, highlightcolor="black")
right_button.grid(row=1, column=0)
wrong_button = Button(image=wrong, highlightthickness=0)
wrong_button.grid(row=1, column=1)

root.mainloop()
