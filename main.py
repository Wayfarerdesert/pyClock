from tkinter import *
from time import *


def update():
    time_string = strftime("%H:%M:%S")
    time_label.config(text=time_string)

    day_string = strftime("%A")
    day_label.config(text=day_string)

    date_string = strftime("%B %d %Y")
    date_label.config(text=date_string)

    window.after(1000, update)


window = Tk()
window.title("Simple Clock")
window.resizable(False, False)
# Set window size
window.geometry("400x250")

time_label = Label(window, font=("Courier", 50), fg="#00FF00", bg="black", height=2)
time_label.pack(fill="x")  # Make the time label occupy the whole width

date_label = Label(window, font=("Courier", 25))
date_label.pack(side="bottom", anchor="center")

day_label = Label(window, font=("Courier", 25))
day_label.pack(side="bottom", anchor="center")

update()

window.mainloop()
