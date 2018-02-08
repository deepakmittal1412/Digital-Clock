from tkinter import *
import time


def update():
    t = time.ctime()
    l.config(text=t)
    root.after(1000, update)


root = Tk()
root.resizable(0, 0)
root.pack_propagate(0)
root.config(height=100, width=250)
root.title("Digital Clock")
frame1 = Frame(root, bg="black", bd=10, relief=SUNKEN)
frame1.pack(expand=YES, fill=BOTH, side=LEFT)
l = Label(frame1, text="PyClock", font=("Helvetica", "12", "italic"), bg="lavender blush")
l.pack(expand=YES, fill=BOTH)
root.after(2000, update)
root.mainloop()
