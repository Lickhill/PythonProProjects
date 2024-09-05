# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
rep = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def resettimercompletely():
    window.after_cancel(timer)
    title.config(text="Timer", fg=GREEN)
    ticks.config(text="")
    canvas.itemconfig(timer_text, text="00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- #


def startTimer():
    global rep
    rep += 1
    if rep == 9:
        return
    elif rep == 8:
        countDownMechanism(1 * 7)
        title.config(text="BREAK", fg=RED)
        ticks.config(text="✔" * (rep / 2))

    elif rep % 2 == 0:
        countDownMechanism(1 * 5)
        title.config(text="BREAK", fg=PINK)
        ticks.config(text="✔" * int(rep / 2))

    elif rep % 2 != 0:
        countDownMechanism(1 * 10)
        title.config(text="WORK", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countDownMechanism(count):

    canvas.itemconfig(timer_text, text=f"{int(count/60):02d}:{int(count%60):02d}")
    if count > 0:
        global timer
        timer = window.after(1000, countDownMechanism, count - 1)
    else:
        startTimer()


# ---------------------------- UI SETUP ------------------------------- #

from tkinter import *

window = Tk()

window.title("Pomodoro Timer")
window.config(padx=100, pady=100, bg=YELLOW)

title = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
title.grid(column=2, row=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomatoImg = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomatoImg)
timer_text = canvas.create_text(
    100, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold")
)


canvas.grid(column=2, row=2)


startButton = Button(text="start", highlightthickness=0, command=startTimer)
startButton.grid(column=1, row=3)

ticks = Label(text="", fg=GREEN, font=(FONT_NAME, 20, "bold"), bg=YELLOW)
ticks.grid(column=2, row=4)

resetbutton = Button(text="reset", highlightthickness=0, command=resettimercompletely)
resetbutton.grid(column=3, row=3)

window.mainloop()
