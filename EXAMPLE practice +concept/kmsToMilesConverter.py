from tkinter import *

window = Tk()

window.title("Kilometers to Miles converter.")
window.minsize(width="500", height="300")
window.config(padx=100, pady=100)

# Use only grid layout
input = Entry()
input.grid(column=2, row=1)

kms = Label(text="kms")
kms.grid(column=3, row=1)

isEqualTo = Label(text="is equal to")
isEqualTo.grid(column=1, row=2)

miles = Label(text=f"0")
miles.grid(column=2, row=2)

kilometers = Label(text="kms")
kilometers.grid(column=3, row=2)


def clickthebutton():
    miles.config(text=f"{int(input.get()) * 1.6}")


button = Button(text="Calculate", command=clickthebutton)
button.grid(column=2, row=3)

window.mainloop()
