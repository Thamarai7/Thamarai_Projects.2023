import math
import tkinter
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
wait = None

# .......................Reset....................
def _reset_():
    t.after_cancel(wait)
    canvas.itemconfig(timer_text, text="00:00")
    check.config(text=" ")
    global reps
    reps = 0


#........................Start....................
def _start_():
    global reps
    reps += 1
    work = WORK_MIN * 60
    short = SHORT_BREAK_MIN * 60
    long = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN)
        timer_label.config(text="Long", fg=RED)
    elif reps % 2 == 0:
        count_down(short)
        timer_label.config(text="Short")
    else:
        count_down(work)
        timer_label.config(text="Work", fg="blue")

#........................Countdown...............


def count_down(count):
    min = math.floor(count / 60)
    sec = (count % 60)
    if sec < 10:
        sec = f"0{sec}"
    canvas.itemconfig(timer_text,  text=f"{min}:{sec}")
    if count > 0:
        global wait
        wait = t.after(1000, count_down, count - 1)
    else:
        _start_()
        marks = " "
        work_time = math.floor(reps/2)
        for _ in range(work_time):
            marks = "✔"
        check.config(text="✔")

# widget
t = tkinter.Tk()
t.title("Pomodoro")
t.config(padx=50, pady=100, bg=YELLOW)


timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35))
timer_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, highlightthickness=0)
image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=image)
timer_text = canvas.create_text(100, 125, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start = Button(text="Start", width=5, command=_start_, highlightthickness=0)
start.grid(column=0, row=2)
reset = Button(text="Reset", width=5,command=_reset_, highlightthickness=0)
reset.grid(column=2, row=2)

check = Label(text=" ", fg=GREEN)
check.grid(column=1, row=3)



t.mainloop()