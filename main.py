from tkinter import *
from time import *


def update():
    time_string = strftime("%H:%M:%S")
    time_label.config(text=time_string)

    day_string = strftime("%A")
    day_label.config(text=day_string)

    time_label.after(1000, update)


window = Tk()
window.resizable(False, False)

time_label = Label(window, font=("Arial", 50), fg="#00FF00", bg="black")
time_label.pack()

day_label = Label(window, font=("Arial", 25))
day_label.pack()

update()

window.mainloop()
