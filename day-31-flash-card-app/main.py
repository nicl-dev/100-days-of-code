import random
import pandas
from tkinter import *

# Set up Window
root = Tk()
root.title("Flash Cards")
root.minsize(width=900, height=626)

# Get the data
data = pandas.read_csv("data/french_words.csv")
data_dict = pandas.DataFrame.to_dict(data, orient="records")
random_entry = random.choice(data_dict)
french_word = random_entry['French']
translation = random_entry['English']

# Constants
BACKGROUND_COLOR = "#B1DDC6"
CARD_BACK_IMAGE = PhotoImage(file="images/card_back.png")
CARD_FRONT_IMAGE = PhotoImage(file="images/card_front.png")
RIGHT_IMAGE = PhotoImage(file="images/right.png")
WRONG_IMAGE = PhotoImage(file="images/wrong.png")

# Window configuration
root.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Canvas
card_canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_canvas.create_image(400, 263, image=CARD_FRONT_IMAGE)
card_canvas.create_text(400, 150, text=french_word, font=("Arial", 40, "italic"))
card_canvas.create_text(400, 263, text=translation, font=("Arial", 60, "bold"))
card_canvas.grid(row=0, column=0, columnspan=2)

# Buttons
right_button = Button(image=RIGHT_IMAGE, highlightthickness=0, highlightcolor="black")
right_button.grid(row=1, column=0)
wrong_button = Button(image=WRONG_IMAGE, highlightthickness=0)
wrong_button.grid(row=1, column=1)

root.mainloop()
