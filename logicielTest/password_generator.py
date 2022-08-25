from random import randint, choice
from tkinter import *
import string
# create a screen
from tkinter import Tk

myScreen = Tk()
myScreen.title("password generator")
myScreen.geometry("800x500")
myScreen.minsize(300, 300)
myScreen.maxsize(800, 500)
myScreen.iconbitmap("testImage.ico")
myScreen.config(bg="#4065A4")

bg = "#4065A4"
# frame
frame = Frame(myScreen, bg=bg)
# create an image
width = 100
height = 100
image = PhotoImage(file="insta.png").zoom(5).subsample(32)
canvas = Canvas(frame, width=width, height=height, bg=bg, bd=0, highlightthickness=0)
canvas.create_image(width / 2, height / 2, image=image)
canvas.grid(row=0, column=0, sticky=W)

# une sous boite
right_frame = Frame(frame, bg=bg)
# label
label_title = Label(right_frame, text="password", font=("helvetica", 20), bg=bg, fg="white")
label_title.pack()


# =====================================================
def generate_password():
    password_min = 11
    password_max = 12
    all_chars = string.ascii_letters
    password = "".join(choice(all_chars) for x in range(randint(password_min, password_max)))
    password_entry.delete(0, END)
    password_entry.insert(0, f"!{password}!")
# =====================================================


password_entry = Entry(right_frame, font=("helvetica", 20), bg=bg, fg="white")
password_entry.pack()

generate_password_button =\
 Button(right_frame, text="generate password", font=("Courrier", 25), bg=bg, command=generate_password)

generate_password_button.pack(pady=20)
# adroit de la frame principal
right_frame.grid(row=0, column=1, sticky=W)
# show the frames
frame.pack(expand=YES)

myScreen.mainloop()
