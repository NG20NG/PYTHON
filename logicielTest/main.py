
from tkinter import *
import webbrowser

myScreen = Tk()
myScreen.title("NG Calculator")
myScreen.geometry("800x500")
myScreen.minsize(300, 300)
myScreen.maxsize(800, 500)
myScreen.iconbitmap("testImage.ico")
myScreen.config(bg="#41B77F")

# create a frame
frame_title = Frame(myScreen, bg="#41B77F", bd=1, relief=SUNKEN)
# label
label_title = Label(frame_title, text="welcome sir", font=("Courrier", 40), bg="#41B77F", fg="white")
label_title.pack()

label_sub_title = Label(frame_title, text="this is my new application", font=("Courrier", 25), bg="#41B77F", fg="white")
label_sub_title.pack()

frame_title.pack(expand=YES)


# def
def open_text():
    webbrowser.open_new("https://nassimproject.netlify.app")


# BTN
button = Button(text="SUBMIT", command=open_text, font=("Courrier", 25), bg="white", fg="#41B77F", relief=FLAT)
button.pack(pady=25, fill=X)


def close_text():
    quit()


# BTN INPUT
input_button = Button()
input_button.pack()

# exit
exitBTN = Button(text="exit", command=close_text)
exitBTN.pack()

# loop
myScreen.mainloop()
