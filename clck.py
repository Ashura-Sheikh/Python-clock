import sys
from tkinter import *
import time

def times():
    current_time = time.strftime("%H:%M:%S")
    clock.config(text=current_time)
    clock.after(200, times)

root = Tk()
root.geometry("500x500")
root.title("Ashura-clock")
root.config(bg="black")

clock = Label(root, font=("times", 50,"bold"), bg="green", fg="white")
clock.grid(row=2, column=1, padx=100, pady=25)
times()

digital = Label(root, text="Digital Clock", font="times 24 bold", bg="green", fg="white")
digital.grid(row=0, column=1, pady=25)

note = Label(root, text="Hours   Minutes  Seconds   ", font="times 15 bold")

root.mainloop()
