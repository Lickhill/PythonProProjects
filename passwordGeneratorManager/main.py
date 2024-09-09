from tkinter import *
from tkinter import messagebox
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import random


def generatePassword():
    letters = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+", "@"]

    nr_letters = random.randint(2, 6)
    nr_symbols = random.randint(2, 6)
    nr_numbers = random.randint(2, 6)

    # Hard Level - Order of characters randomised:
    # e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

    # flist = []
    # for i in range(0, nr_letters):
    #     flist.append(random.choice(letters))

    # for i in range(0, nr_symbols):
    #     flist.append(random.choice(symbols))

    # for i in range(0, nr_numbers):
    #     flist.append(random.choice(numbers))

    flist = (
        [random.choice(letters) for _ in range(nr_letters)]
        + [random.choice(symbols) for _ in range(nr_symbols)]
        + [random.choice(numbers) for _ in range(nr_numbers)]
    )

    random.shuffle(flist)

    # password = ""
    # for i in range(0, len(flist)):
    #     password += flist[i]
    password = "".join(flist)

    passwordInput.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def putData():
    if websiteInput.get() == "" or passwordInput.get() == "" or emailInput.get() == "":
        messagebox.showerror("Error!", "The fields must not remain empty!")
        return
    is_ok = messagebox.askokcancel(
        title="Website Info",
        message=f"Your input details:\n Website: {websiteInput.get()}\n Email: {emailInput.get()}\n Password: {passwordInput.get()}\n Are you sure you want to go with this?",
    )
    if is_ok:
        with open("allPasswords.txt", "a") as file:
            file.write(
                f"{websiteInput.get()} | {emailInput.get()} | {passwordInput.get()}\n"
            )
        websiteInput.delete(0, END)
        passwordInput.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.config(padx=40, pady=40)


window.title("Password Generator and Manager")
lockImage = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200, highlightthickness=0)
canvas.create_image(100, 100, image=lockImage)
canvas.grid(column=1, row=0)

Website = Label(text="Website:")
Website.grid(column=0, row=2)

websiteInput = Entry(width=35)
websiteInput.grid(column=1, row=2, columnspan=2)
websiteInput.focus()

Email = Label(text="Email:")
Email.grid(column=0, row=3)


emailInput = Entry(width=35)
emailInput.grid(column=1, row=3, columnspan=2)
emailInput.insert(0, "likhilnm17103@gmail.com")

password = Label(text="Password:")
password.grid(column=0, row=4)

passwordInput = Entry(width=25)
passwordInput.grid(column=1, row=4)

generateButton = Button(text="Generate and Copy", command=generatePassword)
generateButton.grid(column=2, row=4, sticky="e")


addButton = Button(text="Add", width=29, command=putData)
addButton.grid(column=1, row=5, columnspan=2)


window.mainloop()
