import random
import pandas
from tkinter import *

# Set up Window
root = Tk()
root.title("Flash Cards")
root.minsize(width=900, height=626)

# Constants
BACKGROUND_COLOR = "#B1DDC6"
CARD_BACK_IMAGE = PhotoImage(file="images/card_back.png")
CARD_FRONT_IMAGE = PhotoImage(file="images/card_front.png")
RIGHT_IMAGE = PhotoImage(file="images/right.png")
WRONG_IMAGE = PhotoImage(file="images/wrong.png")

# Window configuration
root.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Get the data
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")
data_dict = pandas.DataFrame.to_dict(data, orient="records")
new_random_entry = {}
first_call = True


def next_card(method):
    global new_random_entry, flip_timer, first_call
    root.after_cancel(flip_timer)
    # If the user knows the translation, remove it from the list of possible words. Store the updated list in a new csv.
    if method == "right":
        data_dict.remove(new_random_entry)
        words_to_learn = pandas.DataFrame(data_dict)
        words_to_learn.to_csv("data/words_to_learn.csv", index=False)
    new_random_entry = random.choice(data_dict)
    card_canvas.itemconfig(card_image, image=CARD_FRONT_IMAGE)
    card_canvas.itemconfig(title, text="French", fill="black")
    card_canvas.itemconfig(word, text=new_random_entry['French'], fill="black")
    flip_timer = root.after(3000, flip_card)


def flip_card():
    card_canvas.itemconfig(title, text="English", fill="white")
    card_canvas.itemconfig(word, text=new_random_entry['English'], fill="white")
    card_canvas.itemconfig(card_image, image=CARD_BACK_IMAGE)


flip_timer = root.after(3000, flip_card)

# Canvas
card_canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_image = card_canvas.create_image(400, 263, image=CARD_FRONT_IMAGE)
title = card_canvas.create_text(400, 150, text="title", font=("Arial", 40, "italic"))
word = card_canvas.create_text(400, 263, text="word", font=("Arial", 60, "bold"))
card_canvas.grid(row=0, column=0, columnspan=2)

# Buttons
right_button = Button(image=RIGHT_IMAGE, highlightthickness=0, highlightcolor="black",
                      command=lambda m="right": next_card(m))
right_button.grid(row=1, column=0)
wrong_button = Button(image=WRONG_IMAGE, highlightthickness=0, command=lambda m="wrong": next_card(m))
wrong_button.grid(row=1, column=1)

next_card("wrong")

root.mainloop()
