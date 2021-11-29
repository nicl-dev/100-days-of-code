from math import floor
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer_running = False
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    global timer_text
    global timer_running
    timer_running = False
    window.after_cancel(timer)
    reps = 0

    timer_label.config(text="Timer")
    completed_timers.config(text="", font=(FONT_NAME, 35, "bold"))
    canvas.itemconfig(timer_text, text=f"00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    global timer_running
    if not timer_running:
        timer_running = True
        reps += 1
        work_sec = WORK_MIN * 60
        short_break_sec = SHORT_BREAK_MIN * 60
        long_break_sec = LONG_BREAK_MIN * 60

        # If it's the 8th rep:
        if reps % 8 == 0:
            timer_label.config(text="Long Break", fg=RED)
            count_down(long_break_sec)
        # If it's the 1st/3rd/5th/7th rep:
        elif reps % 2 == 0:
            timer_label.config(text="Short Break", fg=PINK)
            count_down(short_break_sec)
        # If it's the 2nd/4th/6th rep:
        else:
            timer_label.config(text="Work", fg=GREEN)
            count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer_running
    count_min = floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        timer_running = False
        start_timer()
        total_sessions = reps / 2
        checks = "🗸" * int(total_sessions)
        completed_timers.config(text=checks, font=(FONT_NAME, 35, "bold"))


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=203, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(row=1, column=1)

timer_label = Label(bg=YELLOW, fg=GREEN, text="Timer", font=(FONT_NAME, 35, "bold"))
timer_label.grid(row=0, column=1)

completed_timers = Label(text="", font=(FONT_NAME, 35, "bold"), bg=YELLOW, fg=GREEN)
completed_timers.grid(row=2, column=1)

start_button = Button(text="Start", command=start_timer)
start_button.grid(row=2, column=0)

reset_timer = Button(text="Reset", command=reset_timer)
reset_timer.grid(row=2, column=2)

window.mainloop()
