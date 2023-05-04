import math
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


# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    t.after_cancel(wait)
    canvas.itemconfig(timer_text, text="00:00")
    timer.config(text="Timer")
    check.config(text=" ")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_():
    # count_down(5 * 60)
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break)
        timer.config(text="Long Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break)
        timer.config(text="Short Break", fg=PINK)
    else:
        count_down(work_sec)
        timer.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    min = math.floor(count / 60)
    sec = (count % 60)
    if sec < 10:
        sec = f"0{sec}"
    canvas.itemconfig(timer_text, text=f"{min}:{sec}")
    if count > 0:
        global wait
        wait = t.after(1000, count_down, count - 1)
    else:
        start_()
        marks = " "
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks = "✔"
        check.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #

t = Tk()
t.title("Pomodoro")
t.config(pady=100, padx=50, bg=YELLOW)

timer = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 45))
timer.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, highlightthickness=0)
image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start = Button(text="Start", width=5, command=start_)
start.grid(column=0, row=2)
end = Button(text="End", width=5, command=reset, highlightthickness=0)
end.grid(column=2, row=2)

check = Label(text=" ", fg=GREEN, bg=YELLOW, font=(50))
check.grid(column=1, row=4)

t.mainloop()
